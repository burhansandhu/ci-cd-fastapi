from fastapi import FastAPI

from app.auth.controllers import router as auth_router
from app.users.controllers import router as users_router

app = FastAPI(title="Docker Compose Practice API")


app.include_router(auth_router)
app.include_router(users_router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
