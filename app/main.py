from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI

from app.database import User
from app.schemas import UserCreate, UserRead, UserUpdate
from app.services.auth import auth_backend, current_active_user, fastapi_users, redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await redis.close()


app = FastAPI(lifespan=lifespan)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@app.get("/")
async def root():
    return {"message": "Hello World"}
