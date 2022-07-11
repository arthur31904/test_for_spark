# coding=utf8
from __future__ import unicode_literals

import formencode
import uuid
from formencode import validators, ForEach


class BrandCreateForm(formencode.Schema):
    """使用者建立格式
    name: str
    brand_description: Optional[str] = None
    send_point_description: Optional[str] = None
    brand_intro: Optional[str] = None
    brand_about: Optional[str] = None
    small_logo: Optional[str] = None
    large_logo: Optional[str] = None
    banner_url: Optional[str] = None
    subbrands_img: Optional[str] = None
    subbrands_info: Optional[str] = None
    type: str
    status: str
    alias: str
    code: str
    order_weighting: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    remark: Optional[str] = None
    is_deleted: bool
    is_online: bool
    is_point: bool
    eshop_name: Optional[str] = None
    eshop_url: Optional[str] = None
    foodpanda_url: Optional[str] = None
    facebook_fanpage_url: Optional[str] = None
    line_official_account: Optional[str] = None
    """
    allow_extra_fields = True
    filter_extra_fields = True
    ignore_key_missing = True

    name = validators.String(not_empty=True, strip=True)
    brand_description = validators.String(not_empty=False, strip=True)
    send_point_description = validators.String(not_empty=False, strip=True)
    brand_intro = validators.String(not_empty=True, strip=True)
    brand_about = validators.String(not_empty=True, strip=True)
    small_logo = validators.String(not_empty=True, strip=True)
    large_logo = validators.String(not_empty=True, strip=True)
    banner_url = validators.String(not_empty=False, strip=True)
    subbrands_img = validators.String(not_empty=False, strip=True)
    subbrands_info = validators.String(not_empty=False, strip=True)
    type = validators.String(not_empty=True, strip=True)
    status = validators.String(not_empty=True, strip=True)
    alias = validators.String(not_empty=True, strip=True)
    code = validators.String(not_empty=True, strip=True)
    order_weighting = validators.Int(not_empty=False, strip=True)
    start_date = validators.DateValidator(not_empty=True, strip=True)
    end_date = validators.DateValidator(not_empty=True, strip=True)
    remark = validators.String(not_empty=False, strip=True)
    is_deleted = validators.Bool(not_empty=True, strip=True)
    is_online = validators.Bool(not_empty=True, strip=True)
    is_point = validators.Bool(not_empty=True, strip=True)
    eshop_name = validators.String(not_empty=False, strip=True)
    eshop_url = validators.String(not_empty=False, strip=True)
    foodpanda_url = validators.String(not_empty=False, strip=True)
    facebook_fanpage_url = validators.String(not_empty=False, strip=True)
    line_official_account = validators.String(not_empty=False, strip=True)

class BrandCreateSyncForm(formencode.Schema):
    """使用者建立格式
    name: str
    brand_description: Optional[str] = None
    send_point_description: Optional[str] = None
    brand_intro: Optional[str] = None
    brand_about: Optional[str] = None
    small_logo: Optional[str] = None
    large_logo: Optional[str] = None
    banner_url: Optional[str] = None
    subbrands_img: Optional[str] = None
    subbrands_info: Optional[str] = None
    type: str
    status: str
    alias: str
    code: str
    order_weighting: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    remark: Optional[str] = None
    is_deleted: bool
    is_online: bool
    is_point: bool
    eshop_name: Optional[str] = None
    eshop_url: Optional[str] = None
    foodpanda_url: Optional[str] = None
    facebook_fanpage_url: Optional[str] = None
    line_official_account: Optional[str] = None
    """
    allow_extra_fields = True
    filter_extra_fields = True
    ignore_key_missing = True

    brand_id = validators.Int(not_empty=True, strip=True)
    name = validators.String(not_empty=True, strip=True)
    brand_description = validators.String(not_empty=False, strip=True)
    send_point_description = validators.String(not_empty=False, strip=True)
    brand_intro = validators.String(not_empty=False, strip=True)
    brand_about = validators.String(not_empty=False, strip=True)
    small_logo = validators.String(not_empty=False, strip=True)
    large_logo = validators.String(not_empty=False, strip=True)
    banner_url = validators.String(not_empty=False, strip=True)
    subbrands_img = validators.String(not_empty=False, strip=True)
    subbrands_info = validators.String(not_empty=False, strip=True)
    type = validators.String(not_empty=True, strip=True)
    status = validators.String(not_empty=True, strip=True)
    alias = validators.String(not_empty=True, strip=True)
    code = validators.String(not_empty=True, strip=True)
    order_weighting = validators.Int(not_empty=False, strip=True)
    start_date = validators.DateValidator(not_empty=True, strip=True)
    end_date = validators.DateValidator(not_empty=True, strip=True)
    remark = validators.String(not_empty=False, strip=True)
    is_deleted = validators.Bool(not_empty=True, strip=True)
    is_online = validators.Bool(not_empty=True, strip=True)
    is_point = validators.Bool(not_empty=True, strip=True)
    eshop_name = validators.String(not_empty=False, strip=True)
    eshop_url = validators.String(not_empty=False, strip=True)
    foodpanda_url = validators.String(not_empty=False, strip=True)
    facebook_fanpage_url = validators.String(not_empty=False, strip=True)
    line_official_account = validators.String(not_empty=False, strip=True)


class BrandEditForm(formencode.Schema):
    """AccountEdit 檢查"""
    allow_extra_fields = True
    ignore_key_missing = True

    brand_id = validators.Int(not_empty=True, strip=True)
    name = validators.String(not_empty=True, strip=True)
    brand_description = validators.String(not_empty=False, strip=True)
    send_point_description = validators.String(not_empty=False, strip=True)
    brand_intro = validators.String(not_empty=False, strip=True)
    brand_about = validators.String(not_empty=False, strip=True)
    small_logo = validators.String(not_empty=False, strip=True)
    large_logo = validators.String(not_empty=False, strip=True)
    banner_url = validators.String(not_empty=False, strip=True)
    subbrands_img = validators.String(not_empty=False, strip=True)
    subbrands_info = validators.String(not_empty=False, strip=True)
    type = validators.String(not_empty=True, strip=True)
    status = validators.String(not_empty=True, strip=True)
    alias = validators.String(not_empty=True, strip=True)
    code = validators.String(not_empty=True, strip=True)
    order_weighting = validators.Int(not_empty=False, strip=True)
    start_date = validators.DateValidator(not_empty=True, strip=True)
    end_date = validators.DateValidator(not_empty=True, strip=True)
    remark = validators.String(not_empty=False, strip=True)
    is_deleted = validators.Bool(not_empty=True, strip=True)
    is_online = validators.Bool(not_empty=True, strip=True)
    is_point = validators.Bool(not_empty=True, strip=True)
    eshop_name = validators.String(not_empty=False, strip=True)
    eshop_url = validators.String(not_empty=False, strip=True)
    foodpanda_url = validators.String(not_empty=False, strip=True)
    facebook_fanpage_url = validators.String(not_empty=False, strip=True)
    line_official_account = validators.String(not_empty=False, strip=True)

class BrandGetIdForm(formencode.Schema):
    """AccountEdit 檢查"""
    allow_extra_fields = True
    ignore_key_missing = True

    brand_id = validators.Int(not_empty=True, strip=True)




class BrandSearchForm(formencode.Schema):
    """AccountSearch 檢查"""
    allow_extra_fields = True
    filter_extra_fields = True
    ignore_key_missing = True


    page = validators.Int(not_empty=True, min=1)  # 第幾頁
    limit = validators.Int(not_empty=True, min=1)  # 一頁幾筆

