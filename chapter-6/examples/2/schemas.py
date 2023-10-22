from pydantic import BaseModel


class SignUpDto(BaseModel):
    id: int
    name: str


class UserDto(BaseModel):
    id: int
    name: str

