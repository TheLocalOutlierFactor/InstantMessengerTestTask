from datetime import datetime
import uuid

from fastapi_users import schemas
from pydantic import BaseModel


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class MessageCreate(BaseModel):
    receiver_id: int
    content: str


class MessageInDB(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    content: str
    timestamp: datetime

    class Config:
        from_attributes = True


class MessageOut(BaseModel):
    id: int
    sender: UserRead
    receiver: UserRead
    content: str
    timestamp: datetime

    class Config:
        from_attributes = True
