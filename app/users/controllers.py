from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.auth.models import User
from app.users.dtos import ProfileResponse, ProfileUpdateRequest
from app.users.services import delete_profile, update_profile
from database import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/profile", response_model=ProfileResponse)
def get_profile(
    current_user: User = Depends(get_current_user),
):
    return current_user


@router.put("/profile", response_model=ProfileResponse)
def update_user_profile(
    data: ProfileUpdateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return update_profile(db, current_user, data)


@router.delete("/profile", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    delete_profile(db, current_user)
