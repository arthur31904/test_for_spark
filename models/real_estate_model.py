# coding=utf8
from __future__ import unicode_literals

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ARRAY,
    ForeignKey,
    DateTime,
    Date,
    Boolean
)
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from base.meta_module import (Base, TimestampTable, GUID, uuid4)

class RealEstate(Base, TimestampTable):
    """
    不動產資料表
    """
    __tablename__ = 'real_estate'
    real_estate_id = Column('real_estate_id', Integer, primary_key=True, autoincrement=True
                        , doc=u"不動產流水編號")

    townships = Column('townships', String(100), nullable=True, doc=u"鄉鎮市區")

    transaction_sign = Column('transaction_sign', String(128), nullable=True, doc=u"交易標的")

    house_number_plate = Column('house_number_plate', String, doc=u"土地位置建物門牌")

    total_area_square_meter = Column('total_area_square_meter', Float, doc=u"土地移轉總面積平方公尺")

    use_zoning = Column('use_zoning', String, doc=u"都市土地使用分區")

    non_metropolis_use_district = Column('non_metropolis_use_district', String, doc=u"非都市土地使用分區")

    non_metropolis_land_use = Column('non_metropolis_land_use', String, doc=u"非都市土地使用編定")

    transaction_year_month_day = Column('transaction_year_month_day', Date, doc=u"交易年月日")

    transaction_pen_number = Column('transaction_pen_number', String, doc=u"交易筆棟數")

    shifting_level = Column('shifting_level', String, doc=u"移轉層次")

    total_floor_number = Column('total_floor_number', Integer, doc=u"總樓層數")

    building_state = Column('building_state', String, doc=u"建物型態")

    main_use = Column('main_use', String, doc=u"主要用途")

    main_building_materials = Column('main_building_materials', String, doc=u"主要建材")

    construction_to_complete_the_years = Column('construction_to_complete_the_years', Date, doc=u"建築完成年月")

    building_shifting_total_area = Column('building_shifting_total_area', Float, doc=u"建物移轉總面積平方公尺")

    pattern_room = Column('pattern_room', Integer, doc=u"建物現況格局-房")

    pattern_hall = Column('pattern_hall', Integer, doc=u"建物現況格局-廳")

    pattern_health = Column('pattern_health', Integer, doc=u"建物現況格局-衛")

    pattern_compartmented = Column('pattern_compartmented', Boolean, nullable=False, default=True,
                     doc=u"建物現況格局-隔間")

    manages_the_organization = Column('manages_the_organization', Boolean, nullable=False, default=True,
                     doc=u"有無管理組織")

    total_price = Column('total_price', Integer, nullable=False,
                     doc=u"總價元")

    the_unit_price = Column('the_unit_price', Integer, nullable=True,
                     doc=u"單價元平方公尺")

    the_berth_category = Column('the_berth_category', String, nullable=True,
                     doc=u"車位類別")

    berth_shifting_total_area_square_meter = Column('berth_shifting_total_area_square_meter', Float, nullable=True,
                     doc=u"車位移轉總面積(平方公尺)")

    the_berth_total_price = Column('the_berth_total_price', Integer, nullable=True,
                     doc=u"車位總價元")

    the_note = Column('the_note', String, nullable=True,
                     doc=u"備註")

    serial_number = Column('serial_number', String, nullable=True,
                     doc=u"編號")

    main_building_area = Column('main_building_area', Float, nullable=True,
                     doc=u"主建物面積")

    auxiliary_building_area = Column('auxiliary_building_area', Float, nullable=True,
                     doc=u"附屬建物面積")

    balcony_area = Column('balcony_area', Float, nullable=True,
                     doc=u"陽台面積")

    elevator = Column('elevator', String, nullable=True,
                     doc=u"電梯")

    transfer_number = Column('transfer_number', String, nullable=True,
                     doc=u"移轉編號")



    def __repr__(self):
        return '<RealEstateObject (real_estate_id={0})>'.format(self.real_estate_id)

    @classmethod
    def __getattributes__(cls):
        return [i[1:] if i[:1] == '_' else i for i in cls.__dict__.keys() if
                i[:1] != '_' or i == '_update_user_id' or i == '_create_user_id']

    @classmethod
    def __likeattribute__(cls, key_word):
        map_args = [i for i in cls.__dict__.keys() if key_word in i and i[:1] != '_']
        return map_args[0] if map_args else None

    def __json__(self):
        '''

        '''
        d = {
            'real_estate_id': str(self.real_estate_id),
            'townships': self.townships,
            'transaction_sign': self.transaction_sign,
            'house_number_plate': self.house_number_plate,
            'total_area_square_meter': self.total_area_square_meter,
            'use_zoning': self.use_zoning,
            'non_metropolis_use_district': self.non_metropolis_use_district,
            'non_metropolis_land_use': self.non_metropolis_land_use,
            'transaction_year_month_day': self.transaction_year_month_day,
            'transaction_pen_number': self.transaction_pen_number,
            'shifting_level': self.shifting_level,
            'total_floor_number': self.total_floor_number,
            'building_state': self.building_state,
            'main_use': self.main_use,
            'main_building_materials': self.main_building_materials,
            'construction_to_complete_the_years': self.construction_to_complete_the_years,
            'building_shifting_total_area': self.building_shifting_total_area,
            'pattern_room': self.pattern_room,
            'pattern_hall': self.pattern_hall,
            'pattern_health': self.pattern_health,
            'pattern_compartmented': self.pattern_compartmented,
            'manages_the_organization': self.manages_the_organization,
            'total_price': self.total_price,
            'the_unit_price': self.the_unit_price,
            'the_berth_category': self.the_berth_category,
            'berth_shifting_total_area_square_meter': self.berth_shifting_total_area_square_meter,
            'the_berth_total_price': self.the_berth_total_price,
            'the_note': self.the_note,
            'serial_number': self.serial_number,
            'main_building_area': self.main_building_area,
            'auxiliary_building_area': self.auxiliary_building_area,
            'balcony_area': self.balcony_area,
            'elevator': self.elevator,
            'transfer_number': self.transfer_number
        }


        return d