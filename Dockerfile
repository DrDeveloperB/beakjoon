# 베이스 이미지 설정
FROM python:3.9.13

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# 애플리케이션 파일 복사
# Flask
# COPY flask_main.py .
# FastAPI
COPY fastapi_main.py .

# output 디렉토리 생성
RUN mkdir /data

# 애플리케이션 실행
# Flask
# CMD ["python", "flask_main.py"]
# FastAPI
CMD ["python", "fastapi_main.py"]
