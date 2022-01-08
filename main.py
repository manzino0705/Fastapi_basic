from typing import Optional
from fastapi import FastAPI

app = FastAPI() # 서버 인스턴스 생성 

@app.get("/")
def read_root():
    return {"Hello": "World"}