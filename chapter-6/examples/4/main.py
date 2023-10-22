import time

import uvicorn
from fastapi import FastAPI, Request

import users
from config import config

app = FastAPI(title="Python Course", description="Base Template for learning FastAPI")
app.include_router(users.router)


@app.get("/")  # method + path
async def say_hello():  # async/sync + name in docs
    return {"message": "Hello World"}  # response


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    # time.sleep(1)
    process_time = time.time() - start_time
    print(process_time)
    response.headers["X-Process-Time"] = str(process_time)
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host=config.server_host, port=config.server_port, reload=True)
    # http://localhost:8000/docs
