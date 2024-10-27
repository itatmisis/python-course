import uvicorn
from app import app
from settings import settings

uvicorn_app = app

if __name__ == "__main__":
    uvicorn.run(
        "entrypoint:uvicorn_app",
        host=settings.server_host,
        port=settings.server_port,
        workers=settings.server_workers,
    )
