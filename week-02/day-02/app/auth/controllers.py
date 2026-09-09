from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import dtos, services
from database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(
    data: dtos.SignupRequest,
    db: Session = Depends(get_db),
):
    user = services.create_user(
        db=db,
        email=data.email,
        username=data.username,
        full_name=data.full_name,
        password=data.password,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email or username already exists",
        )

    return {
        "message": "User created successfully",
        "user_id": user.id,
    }


@router.post("/login", response_model=dtos.TokenResponse)
def login(
    data: dtos.LoginRequest,
    db: Session = Depends(get_db),
):
    user = services.authenticate_user(
        db=db,
        email=data.email,
        password=data.password,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = services.create_access_token(user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
