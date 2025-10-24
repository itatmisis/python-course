from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel
from services.link_service import LinkService


def create_app() -> FastAPI:
    app = FastAPI()
    short_link_service = LinkService()

    class PutLink(BaseModel):
        link: str

    def _service_link_to_real(short_link: str) -> str:
        return f"http://localhost:8000/{short_link}"

    @app.post("/link")
    async def create_link(put_link_request: PutLink) -> PutLink:
        short_link = await short_link_service.create_link(put_link_request.link)
        return PutLink(link=_service_link_to_real(short_link))

    @app.get("/{link}")
    async def get_link(link: str) -> Response:
        real_link = await short_link_service.get_real_link(link)

        if real_link is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Short link not found:(")

        return Response(status_code=status.HTTP_301_MOVED_PERMANENTLY, headers={"Location": real_link})

    return app
