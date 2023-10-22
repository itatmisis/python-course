from pydantic import BaseModel, Field


class SignUpDto(BaseModel):
    id: int
    name: str


class UserDto(BaseModel):
    id: int
    name: str = Field(default="Jane Doe", description="Name of user")

