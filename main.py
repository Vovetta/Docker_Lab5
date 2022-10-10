from asyncio import run

from hypercorn.asyncio import serve, Config
from fastapi import FastAPI
from fastapi.routing import APIRoute

from api.counter import root, about, stat

app = FastAPI(routes=[
    APIRoute('/about', about, methods=['GET']),
    APIRoute('/stat', stat, methods=['GET']),
    APIRoute('/', root, methods=['GET'])
])

if __name__ == '__main__':
    config = Config()
    config.bind = '0.0.0.0:8000'
    config.accesslog = '-'
    config.errorlog = '-'
    run(serve(app, config))  # type: ignore
