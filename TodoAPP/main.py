# from typing import Annotated
# from sqlalchemy.orm import session
from fastapi import FastAPI, Depends
import models
from database import engine, SessionalLocal


app=FastAPI()

models.Base.metadata.create_all(bind=engine)


# def get_db():
#     db=SessionLocal()
#     try: 
#         yield db
#     finally: 
#         db.close()

# db_dependency=Annotated[session,Depends(get_db)]
# @app.get("/")
# async def read_all(db:db_dependency):
#     return db.query(Todos).all()