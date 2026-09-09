from pydantic import BaseModel, EmailStr


class ProfileUpdateRequest(BaseModel):
    username: str | None = None
    full_name: str | None = None
    email: EmailStr | None = None


class ProfileResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    full_name: str

    model_config = {"from_attributes": True}
