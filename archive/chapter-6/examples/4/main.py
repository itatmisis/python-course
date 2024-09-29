import time
from collections.abc import Awaitable, Callable

import users
import uvicorn
from config import config
from fastapi import FastAPI, Request, Response

app = FastAPI(title="Python Course", description="Лучший шаблон, чтобы учить FastAPI")
app.include_router(users.router)


# response_model - возвращаемая модель данных
@app.get("/", response_model=dict[str, str])  # endpoint = method + path
def say_hello() -> dict[str, str]:  # имя функции будет использоваться в документации
    """
    Текст в документаци функции будет использоваться в сваггере
    """
    return {"message": "Hello World"}  # ответ


@app.middleware("http")
async def add_process_time_header(request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host=config.server_host, port=config.server_port, reload=True)
    # http://localhost:8000/docs
