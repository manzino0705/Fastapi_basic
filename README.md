# Fastapi_basic


### 초기 setting 

**1. 가상환경 설정** <br>
python -m venv venv<br>
python -m pip install --upgrade pip <br><br>


**2. fast api 설치** <br>
pip install fastapi <br>
pip install uvicorn<br><br>

**3. fast api 실행** <br>
uvicorn main:app --reload   // --reload : 파일 변경시, 감지해서 재시작 
-> http://127.0.0.1:8000 으로 바로 접근 가능 <br>
-> http://127.0.0.1:port/docs : 자동 대화형 API 설명서 <br>

<br><br>