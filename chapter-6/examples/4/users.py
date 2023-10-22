from fastapi import APIRouter, HTTPException

from schemas import UserDto, SignUpDto


router = APIRouter(prefix="/users", tags=["user"])
users: dict[int, UserDto] = {0: UserDto(id=0, name="Jane Doe")}


@router.post("/sign-up", response_model=int)
async def sign_up(sign_up_request: SignUpDto):
    user = UserDto(id=len(users) + 1, name=sign_up_request.name)
    users[user.id] = user
    return user.id


@router.get("/{user_id}", response_model=UserDto)
async def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователя не существует")
    return users.get(user_id, None)

# editor will show error
# @router.get("/users/")
# async def get_user(skip: int = 0, limit: int = 10) -> list[UserDto]:
#     users_after_skip = users.values()[skip:]
#     needed_users = users_after_skip[:limit]
#     return needed_users


@router.get("/users/", response_model=list[UserDto])
async def get_user(skip: int = 0, limit: int = 10):
    users_after_skip = users.values()[skip:]
    needed_users = users_after_skip[:limit]
    return needed_users

