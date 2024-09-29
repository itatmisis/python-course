import uvicorn
from fastapi import FastAPI, HTTPException, Path, status
from schemas import SignUpDto, UserDto

app = FastAPI(title="Python Course", description="Лучший шаблон, чтобы учить FastAPI")
users: list[UserDto] = []


# response_model - возвращаемая модель данных
@app.get("/", response_model=dict[str, str])  # endpoint = method + path
def say_hello() -> dict[str, str]:  # имя функции будет использоваться в документации
    """
    Текст в документаци функции будет использоваться в сваггере
    """
    return {"message": "Hello World"}  # ответ


@app.post("/users/sign-up", response_model=int)
def sign_up(sign_up_request: SignUpDto) -> int:
    user_id = len(users)
    user = UserDto(id=user_id, name=sign_up_request.name)

    users.append(user)
    return user.id


@app.get("/users/{user_id}")
def get_user(user_id: int = Path(...)) -> UserDto:
    try:
        return users[user_id]
    except IndexError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found for {user_id=}") from exc


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
