from sqlalchemy.orm import Session

from app.auth.models import User
from app.users.dtos import ProfileUpdateRequest


def update_profile(
    db: Session,
    user: User,
    data: ProfileUpdateRequest,
) -> User:
    if data.username is not None:
        user.username = data.username

    if data.full_name is not None:
        user.full_name = data.full_name

    if data.email is not None:
        user.email = data.email

    db.commit()
    db.refresh(user)

    return user


def delete_profile(db: Session, user: User) -> None:
    db.delete(user)
    db.commit()
