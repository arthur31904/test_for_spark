# coding=utf8
from __future__ import unicode_literals

from sqlalchemy.orm import Session
import transaction
from schemas import real_estate_schema
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from services.real_estate_services import RealEstateService
from from_set import real_estate_form as form
import requests
from fastapi_utils.cbv import cbv

from fastapi_utils.inferring_router import InferringRouter
from zipfile import ZipFile
## 引入回傳值定義
from schemas.response import SuccessResponse, ErrorResponse
import os
from schemas.real_estate_schema import real_estate_back, real_estate_back_list

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

        data_path = "/Users/nagi/python_project/test_work/python_files"

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
    def get_list_spark(self,townships: str, total_floor_number: int, building_state: str):
        """
        搜尋廠商
        """

        data_path = "/Users/nagi/python_project/test_work/python_files/"

        use_list = ['/Users/nagi/python_project/test_work/python_files/a_lvr_land_a.csv',
                    '/Users/nagi/python_project/test_work/python_files/b_lvr_land_a.csv',
                    '/Users/nagi/python_project/test_work/python_files/e_lvr_land_a.csv',
                    '/Users/nagi/python_project/test_work/python_files/f_lvr_land_a.csv',
                    '/Users/nagi/python_project/test_work/python_files/h_lvr_land_a.csv']

        dataFrame = pd.concat(map(pd.read_csv, use_list), ignore_index=True)

        dataFrame = dataFrame.drop(index=0)

        df = dataFrame.replace(pd.NA, '')

        sparkDF = spark.createDataFrame(df)
        sparkDF.printSchema()
        sparkDF.show()

        real_estate_obj_list = {

        }

        return {
            'real_estate_obj_list': real_estate_obj_list
        }
