# step 1) DB와 연결하기 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json 

# 1. db url 생성 
DB_URL = "mysql+pymysql://root:1234@localhost:3306/test_db"
# "postgresql://user:password@postgresserver/db"
# "sqlite:///./sql_app.db"

# SQLAlchemy engine 생성 ( main.py에서 사용)
engine = create_engine( DB_URL, encoding='utf-8' )
# DB session 만들기 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# DB model 생성 
Base = declarative_base()

