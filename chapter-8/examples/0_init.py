from database import engine
from models import Base

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
