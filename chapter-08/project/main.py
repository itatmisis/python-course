import uvicorn
from presentations.fastapi_app import create_app
from settings.settings import settings


def main() -> None:
    uvicorn.run(create_app(), host=settings.uvicorn.host, port=settings.uvicorn.port)


if __name__ == "__main__":
    main()
