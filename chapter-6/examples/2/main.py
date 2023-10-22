import uvicorn
from fastapi import FastAPI

from schemas import UserDto, SignUpDto

app = FastAPI(title="Python Course", description="Base Template for learning FastAPI")
users: dict[int, UserDto] = {0: UserDto(id=0, name="Jane Doe")}


@app.get("/")  # method + path
async def say_hello():  # async/sync + name in docs
    return {"message": "Hello World"}  # response


@app.post("/users/sign-up")
async def sign_up(sign_up_request: SignUpDto) -> int:
    user = UserDto(id=len(users) + 1, name=sign_up_request.name)
    users[user.id] = user
    return user.id

@app.get("/users/{user_id}")
async def get_user(user_id: int) -> UserDto | None:
    return users.get(user_id, None)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)  # base url
    # http://localhost:8000/docs
