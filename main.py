from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from logging.config import dictConfig
from core.logger import LogConfig
from api.health import health_router
from api.v1.api import api_router
from core.config import settings

from database import get_db_session, Engine

from models import test_model,test_model2
# from models import test_model
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from database import SessionLocal, Engine
import os
import transaction
## 引入services
from services.service_services import ServiceService

from base.base_models import (
    get_session_factory,
    get_tm_session,
)


dictConfig(LogConfig().dict())

app = FastAPI(
    root_path = os.getenv('SET_APISIX_URL'),
    title='test_work'
)

## 建立種子資料
engine = Engine
session_factory = get_session_factory(engine)
dbsession = get_tm_session(session_factory, transaction.manager)


service_service = ServiceService(dbsession)

seed_service = [
{
  "name": "NFT",
  "code": "NFT"
},
{
  "name": "POINT",
  "code": "POINT"
},
{
  "name": "TICKET",
  "code": "TICKET"
},
{
  "name": "CASHFLOW",
  "code": "CASHFLOW"
},
{
  "name": "BNPL",
  "code": "BNPL"
}
]

for ser in seed_service:
    check = service_service.get_by(db=dbsession, **ser)
    if check ==None:
        service_service.create(db=dbsession, **ser)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(health_router, tags=["Health"])

app.include_router(api_router, prefix="/api")
