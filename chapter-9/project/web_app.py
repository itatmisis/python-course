import asyncio

import uvicorn
from presentations.fastapi_app import app
from settings.settings import settings


async def main() -> None:
    server = uvicorn.Server(
        uvicorn.Config(
            app,
            host=settings.uvicorn.host,
            port=settings.uvicorn.port,
            workers=settings.uvicorn.workers,
        )
    )
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
