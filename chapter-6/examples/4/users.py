from fastapi import APIRouter, Query

from schemas import SignUpDto, UserDto

router = APIRouter(prefix="/users", tags=["user"])
users: list[UserDto] = []


@router.post("/sign-up", response_model=int)
async def sign_up(sign_up_request: SignUpDto) -> int:
    user_id = len(users)
    user = UserDto(id=user_id, name=sign_up_request.name)

    users.append(user)
    return user.id_


@router.get("/{user_id}", response_model=UserDto | None)
def get_user_by_id(user_id: int) -> UserDto | None:
    try:
        return users[user_id]
    except IndexError:
        return None


@router.get("/", response_model=list[UserDto])
def get_users(offset: int = Query(0), limit: int = Query(10)) -> list[UserDto]:
    return users[offset:limit]
