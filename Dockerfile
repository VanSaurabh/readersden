FROM python:3.10-alpine

WORKDIR /app

ADD requirements.txt .
ADD src/ .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]