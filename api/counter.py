from os import getenv

from socket import gethostname
from fastapi.responses import PlainTextResponse, HTMLResponse


class Counter:
    number = 0

    @classmethod
    async def increment(cls):
        cls.number += 1
        return cls.number

    @classmethod
    async def value(cls):
        return cls.number


async def root():
    return PlainTextResponse(f'{await Counter.value()}')


async def stat():
    return PlainTextResponse(f'{await Counter.increment()}')


async def about():
    html = f'<h3>Hello, {getenv("NAME", "world")}!</h3>' \
           f'<b>Hostname:</b> {gethostname()}<br/>'
    return HTMLResponse(html)
