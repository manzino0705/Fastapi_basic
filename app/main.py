from typing import Optional
from fastapi import FastAPI

app = FastAPI() # 서버 인스턴스 생성 

'''
@app.get("/")  : 데이터 읽기 
@app.post("/") : 데이터 생성 
@app.put("/")  : 데이터 업데이트 
@app.delete("/") : 데이터 삭제 
'''

@app.get("/")
def root():
    return {"Hello": "World"} 

# 경로 매개변수 지정 
# http://127.0.0.1:8000/items/3 
@app.get("/items/{item_id}")  
def read_item(item_id):
    return {"item_id": item_id}

# 쿼리 매개변수 
# http://127.0.0.1:8000/items/?skip=0&limit=2
items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
def read_item(skip: int = 0, limit: int = 10):  # default 지정 가능 
    return items_db[skip : skip + limit]

