import users
import uvicorn
from config import config
from fastapi import FastAPI

app = FastAPI(title="Python Course", description="Лучший шаблон, чтобы учить FastAPI")
app.include_router(users.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host=config.server_host, port=config.server_port, reload=True)
    # http://localhost:8000/docs
