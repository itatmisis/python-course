from fastapi import Depends, FastAPI, Request
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, ConfigDict, Field
from repository import User as UserDB
from repository import get_db
from sqlalchemy import select
from sqlalchemy.orm import Session

app = FastAPI()


@app.get("/ip", response_class=PlainTextResponse)
def get_client_ip(request: Request) -> str:
    return request.client.host


class User(BaseModel):
    id_: int = Field(..., alias="id")
    name: str

    model_config = ConfigDict(from_attributes=True, json_schema_extra={"examples": [{"name": "Anne Frank", "id": 0}]})


@app.get("/users", response_model=list[User])
def get_users(db: Session = Depends(get_db)) -> list[User]:
    rows = db.execute(select(UserDB)).scalars().all()
    return [User.from_orm(row) for row in rows]
