# Fastapi_basic

### FastAPI 기본 구조 Study 
<br>

### 초기 setting 

**1. 가상환경 설정** <br>
```python
python -m venv venv
python -m pip install --upgrade pip 
```

**2. fast api 설치** <br>
```python
pip install fastapi <br>
pip install uvicorn<br>
```

**3. fast api 실행** <br>
```python
uvicorn main:app --reload   # --reload : 파일 변경시, 감지해서 재시작 
```
#### -> http://127.0.0.1:8000 으로 바로 접근 가능 <br>
#### -> http://127.0.0.1:port/docs : 자동 대화형 API 설명서 <br>


<br><br>