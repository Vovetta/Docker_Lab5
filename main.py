from asyncio import run
from datetime import datetime

from hypercorn.asyncio import serve, Config
from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.requests import Request
from sqlalchemy import insert

from api.counter import root, about, stat
from config import Service
from models import RequestInfo
from service.database import DatabaseConnection

app = FastAPI(routes=[
    APIRoute('/about', about, methods=['GET']),
    APIRoute('/stat', stat, methods=['GET']),
    APIRoute('/', root, methods=['GET'])
])
app.add_event_handler('startup', DatabaseConnection.open)


@app.middleware(middleware_type='http')
async def user_tracker(request: Request, call_next):
    async with DatabaseConnection.engine.begin() as connection:
        await connection.execute(
            insert(RequestInfo).values(
                request_dt=datetime.now(),
                user_agent=request.headers.get('user-agent', 'empty user_agent')
            )
        )
    return await call_next(request)


if __name__ == '__main__':
    config = Config()
    config.bind = f'{Service.host}:{Service.port}'
    config.accesslog = '-'
    config.errorlog = '-'
    run(serve(app, config))  # type: ignore
