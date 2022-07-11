from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
"""
基礎為必填
id: int
name = 'John Doe' 
signup_ts: Optional[datetime] = None（選填）
friends: List[int] = [] 預設為空
"""
class brand_create(BaseModel):
    """

    """
    name: str
    brand_description: Optional[str] = None
    send_point_description: Optional[str] = None
    brand_intro: Optional[str] = None
    brand_about: Optional[str] = None
    small_logo: Optional[str] = ""
    large_logo: Optional[str] = ""

    banner_url: Optional[str] = None
    subbrands_img: Optional[str] = None
    subbrands_info: Optional[str] = None
    type:  Optional[str] = "general"
    status: Optional[str] = "normal"
    alias: str
    code: str
    order_weighting: Optional[int] = None
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

class brand_search(BaseModel):
    page: int
    limit: int

from typing import Optional, Any

class real_estate_back(BaseModel):
    """


    """
    brand_id: int
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
    order_weighting: Optional[int] = None
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

class real_estate_back_list(BaseModel):
    """


    """
    real_estate: List[real_estate_back]


class SuccessResponseforcreate(BaseModel):
    success = True
    acb = True
    message: Optional[Any] = None


class ErrorResponse(BaseModel):
    success = False
    message: Optional[Any] = None