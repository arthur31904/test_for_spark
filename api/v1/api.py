from fastapi import APIRouter
from .real_estate import real_estate_views

api_router = APIRouter()


api_router.include_router(real_estate_views.router, prefix="/real_estate_api", tags=["real_estate_api"])
