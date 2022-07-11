from database import Engine
from models import real_estate_model

real_estate_model.Base.metadata.create_all(bind=Engine)
