from fastapi import FastAPI, HTTPException, Header, Path, Response, status, Depends, Request
from pydantic import BaseModel
from services.short_link_service import ShortLinkService

app = FastAPI(title="Наше первое приложение!", description="Прикольное приложение для генерации коротких ссылок")
short_link_service = ShortLinkService()


class PutLink(BaseModel):
    link: str


def _service_link_to_real(short_link: str) -> str:
    return f"http://localhost:8000/short/{short_link}"


@app.put("/link")
async def put_link(put_link_request: PutLink, request: Request, user_agent: str = Header(...)) -> PutLink:

    short_link = await short_link_service.put_link(
        put_link_request.link, created_by_ip=request.client.host, created_by_user_agent=user_agent
    )
    return PutLink(link=_service_link_to_real(short_link))


@app.get("/short/{link}")
async def get_link(request: Request, link: str = Path(...), user_agent: str = Header(...)) -> Response:
    real_link = await short_link_service.get_real_link(link, user_ip=request.client.host, user_agent=user_agent)

    if real_link is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Short link not found:(")

    return Response(status_code=status.HTTP_301_MOVED_PERMANENTLY, headers={"Location": real_link})
