import uvicorn
from presentations.fastapi_app import create_app


def main() -> None:
    uvicorn.run(create_app(), host="localhost", port=8000)


if __name__ == "__main__":
    main()
