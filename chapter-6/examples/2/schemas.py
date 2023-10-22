from pydantic import BaseModel, Field


# DTO - data transfare object, объект, который используется для передачи информации.
class SignUpDto(BaseModel):
    name: str

    model_config = {"json_schema_extra": {"examples": [{"name": "Anne Frank"}]}}


class UserDto(BaseModel):
    id_: int = Field(..., description="Identifier", alias="id")
    name: str

    model_config = {"json_schema_extra": {"examples": [{"name": "Anne Frank", "id": 0}]}}
