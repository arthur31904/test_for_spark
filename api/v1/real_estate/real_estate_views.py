# coding=utf8
from __future__ import unicode_literals

from sqlalchemy.orm import Session
import transaction
from schemas import real_estate_schema
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from services.real_estate_services import RealEstateService
from from_set import real_estate_form as form
import requests
from lib import chinesetointeger
from fastapi_utils.cbv import cbv

from fastapi_utils.inferring_router import InferringRouter
from zipfile import ZipFile
## 引入回傳值定義
from schemas.response import SuccessResponse, ErrorResponse
import os
from schemas.real_estate_schema import real_estate_back, real_estate_back_list
import json
import pandas as pd

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

EstateBackResponses = {
    200: {"model": real_estate_back},
    400: {"model": ErrorResponse},
    404: {"model": ErrorResponse},
    500: {"model": ErrorResponse},
}

EstateBackListResponses = {
    200: {"model": real_estate_back_list},
    400: {"model": ErrorResponse},
    404: {"model": ErrorResponse},
    500: {"model": ErrorResponse},
}

# router = APIRouter()
router = InferringRouter()


def get_db(request: Request):
    return request.state.db


@cbv(router)
class BrandJsonView():
    def __init__(self):
        super(BrandJsonView, self).__init__()
        BrandJsonView.INSTANCE = self
        db: Session = Depends(get_db)
        self.real_estate_services = RealEstateService(session=db)

    @router.get("/crawler")
    def create(self, db: Session = Depends(get_db)):
        """
        創建廠商
        """
        ## 下載檔案
        url = "https://plvr.land.moi.gov.tw/DownloadSeason?season=108S2&type=zip&fileName=lvr_landcsv.zip"
        r = requests.get(url)

        ## 儲存檔案
        file_name = "lvr_landcsv" + '.zip'
        f = open(file_name, 'wb')
        block_sz = 8192

        buffer = r.content

        f.write(buffer)
        f.close()

        data_path = "/test_work/python_files"

        with ZipFile(file_name) as myzip:
            myzip.extractall(data_path)

        for roots, dirs, files in os.walk(data_path):
            for each in files:
                if each in ['a_lvr_land_a.csv', 'b_lvr_land_a.csv', 'e_lvr_land_a.csv', 'f_lvr_land_a.csv',
                            'h_lvr_land_a.csv']:
                    classes = open(roots + '/' + each, 'r').read()

        return "ok"




    @router.get("/get_list", responses=EstateBackListResponses)
    def get_list(self,townships: str, total_floor_number: int, building_state: str, db: Session = Depends(get_db)):
        """
        搜尋廠商
        """
        request_data = {
            "townships":townships,
            "total_floor_number":total_floor_number,
            "building_state":building_state
        }

        real_estate_list, total_count = self.real_estate_services.get_list(db=db, show_count=True, **request_data)

        real_estate_obj_list = [a.__json__() for a in real_estate_list]

        return {
            'real_estate_obj_list': real_estate_obj_list,
            'total_count': total_count
        }

    @router.get("/get_list/spark", responses=EstateBackListResponses)
    def get_list_spark(self,mainuse: str, total_floor_number: int, building_state: str):
        """
        搜尋廠商
        """


        ## 整理爬蟲資料
        use_list = ['/test_work/python_files/a_lvr_land_a.csv',
                    '/test_work/python_files/b_lvr_land_a.csv',
                    '/test_work/python_files/e_lvr_land_a.csv',
                    '/test_work/python_files/f_lvr_land_a.csv',
                    '/test_work/python_files/h_lvr_land_a.csv']

        ## 合併 dataFrame
        dataFrame = pd.concat(map(pd.read_csv, use_list), ignore_index=True)

        ## 去除 dataFrame 第一欄
        dataFrame = dataFrame.drop(index=0)

        ## 去除 dataFrame 空直
        df = dataFrame.replace(pd.NA, '')

        tai = ["中正區",
               "萬華區",
               "大同區",
               "中山區",
               "松山區",
               "大安區",
               "信義區",
               "內湖區",
               "南港區",
               "士林區",
               "北投區",
               "文山區"]

        new_tai = ["板橋區", "中和區", "新莊區", "土城區", "汐止區", "鶯歌區", "淡水區", "五股區", "林口區",
                   "深坑區", "坪林區", "石門區", "萬里區", "雙溪區", "烏來區", "三重區", "永和區", "新店區",
                   "蘆洲區", "樹林區", "三峽區", "瑞芳區", "泰山區", "八里區", "石碇區", "三芝區", "金山區",
                   "平溪區", "貢寮區"]

        toyu = ["桃園區", "八德區", "龜山區", "蘆竹區", "大園區", "大溪區", "中壢區", "平鎮區", "楊梅區", "龍潭區", "新屋區", "觀音區", "復興區"]
        goyu = ["鹽埕區", "鼓山區", "左營區", "楠梓區",
                "三民區", "新興區", "前金區", "苓雅區",
                "前鎮區", "旗津區", "小港區", "鳳山區",
                "林園區", "大寮區", "大樹區", "大社區",
                "仁武區", "鳥松區", "岡山區", "橋頭區",
                "燕巢區", "阿蓮區", "路竹區", "湖內區",
                "茄萣區", "梓官區", "旗山區", "美濃區",
                "六龜區", "甲仙區", "杉林區", "內門區",
                "茂林區", "桃源區", "那瑪夏區", "田寮區",
                "永安區", "彌陀區"]
        taich = ["中區", "東區", "西區", "南區", "北區", "西屯區", "南屯區", "北屯區", "豐原區", "大里區", "太平區", "清水區", "沙鹿區", "大甲區", "東勢區",
                 "梧棲區", "烏日區", "神岡區", "大肚區", "大雅區", "后里區", "霧峰區", "潭子區", "龍井區", "外埔區", "和平區", "石岡區", "大安區", "新社區"]


        ## 轉換 樓層 成 數字，並賦予縣市
        for a in range(len(df)):
            df.loc[int(a + 1), "總樓層數"] = chinesetointeger.chinesetointeger(df.loc[int(a + 1)]['總樓層數'])
            df.loc[int(a + 1), "交易年月日"] = chinesetointeger.changeyear(df.loc[int(a + 1)]['交易年月日'])
            if df.loc[int(a + 1), "鄉鎮市區"] in tai:
                city = "台北市"
            elif df.loc[int(a + 1), "鄉鎮市區"] in new_tai:
                city = "新北市"

            elif df.loc[int(a + 1), "鄉鎮市區"] in toyu:
                city = "桃園市"

            elif df.loc[int(a + 1), "鄉鎮市區"] in goyu:
                city = "高雄市"
            else:
                city = "台中市"
            df.loc[int(a + 1), "縣市"] = city

        sparkDF = spark.createDataFrame(df)

        ## 搜尋 物件
        new_df = sparkDF.filter(sparkDF['主要用途'] == mainuse).filter(sparkDF['建物型態'] == building_state).filter(sparkDF['總樓層數'] >= total_floor_number )

        ## 物件 轉換
        pandas_df = new_df.toPandas()
        ## 資料拆分
        group_obj = pandas_df.groupby(['縣市'])

        ## result-part1
        result_check1 = []
        result_part1 = {

        }
        ## result-part2

        result_part2 = {

        }


        '''
        {
        "date":"",
        "events":[
            {
                "district":"",
                "building_state":""
            }
        ]
        }
        '''
        use_city_list = ["台北市","新北市","桃園市","高雄市","台中市"]



        for city in use_city_list:
            mediation_date = {

            }
            for b in range(len(group_obj.get_group(city))):

                if city not in result_check1 and len(result_check1)<=2:
                    this_obj = group_obj.get_group(city).loc[b, '交易年月日']

                    if this_obj in mediation_date:

                        in_obj = {
                            "district":group_obj.get_group(city).loc[b, '鄉鎮市區'],
                            "building_state":group_obj.get_group(city).loc[b, '建物型態']
                        }

                        mediation_date[this_obj].append(in_obj)
                    else:
                        mediation_date[this_obj] = []
                        in_obj = {
                            "district":group_obj.get_group(city).loc[b, '鄉鎮市區'],
                            "building_state":group_obj.get_group(city).loc[b, '建物型態']
                        }
                        mediation_date[this_obj].append(in_obj)

                    time_slots = []

                    new_list = sorted(mediation_date.keys())

                    for mi in new_list:
                        out_obj = {
                            "date":mi,
                            "events":mediation_date[mi]
                        }
                        time_slots.append(out_obj)


                    result_part1[city] = {
                        "city":city,
                        "time_slots":time_slots
                    }
                    result_check1.append(city)
                else:
                    this_obj = group_obj.get_group(city).loc[b, '交易年月日']

                    if this_obj in mediation_date:

                        in_obj = {
                            "district": group_obj.get_group(city).loc[b, '鄉鎮市區'],
                            "building_state": group_obj.get_group(city).loc[b, '建物型態']
                        }

                        mediation_date[this_obj].append(in_obj)
                    else:
                        mediation_date[this_obj] = []
                        in_obj = {
                            "district": group_obj.get_group(city).loc[b, '鄉鎮市區'],
                            "building_state": group_obj.get_group(city).loc[b, '建物型態']
                        }
                        mediation_date[this_obj].append(in_obj)

                    time_slots = []

                    new_list = sorted(mediation_date.keys())

                    for mi in new_list:
                        out_obj = {
                            "date": mi,
                            "events": mediation_date[mi]
                        }
                        time_slots.append(out_obj)


                    result_part2[city] = {
                        "city": city,
                        "time_slots": time_slots
                    }

        return {
            'result_part1': json.dumps(result_part1),
            'result_part2': json.dumps(result_part2)
        }
