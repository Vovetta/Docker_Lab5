FROM python:3.10-alpine

WORKDIR /app

COPY . .

ENV NAME=Voldemar

RUN pip install wheel setuptools && pip install -r requirements.txt

RUN chmod +x run wait-for

CMD ["python", "main.py"]