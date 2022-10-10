FROM python:3.10-alpine

WORKDIR /app

COPY . .

ENV NAME=Voldemar

RUN pip install wheel
RUN pip install -r requirements.txt

CMD ["python", "main.py"]