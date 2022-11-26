FROM python:3.10-alpine

WORKDIR /app

COPY . .

ENV NAME=Voldemar

RUN chmod +x run wait-for

RUN pip install wheel setuptools && pip install -r requirements.txt

CMD ["python", "main.py"]