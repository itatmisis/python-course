from database import get_db
from fastapi import APIRouter, Depends, Query
from models import User
from schemas import SignUpDto, UserDto
from sqlalchemy import select
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["user"])
users: list[UserDto] = []


@router.post("/sign-up", response_model=int)
async def sign_up(sign_up_request: SignUpDto, db: Session = Depends(get_db)) -> int:
    user = User(**sign_up_request.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user.id


@router.get("/{user_id}", response_model=UserDto | None)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)) -> UserDto | None:
    query = select(User).where(User.id == user_id).limit(1)
    user = db.execute(query).scalar()
    if user is None:
        return None
    return user


@router.get("/", response_model=list[UserDto])
def get_users(offset: int = Query(0), limit: int = Query(10), db: Session = Depends(get_db)) -> list[UserDto]:
    query = select(User).offset(offset).limit(limit)

    return db.execute(query).scalars()
