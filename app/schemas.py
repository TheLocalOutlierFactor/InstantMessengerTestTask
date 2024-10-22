from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class UserInDB(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str


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
        orm_mode = True


class MessageOut(BaseModel):
    id: int
    sender: UserInDB
    receiver: UserInDB
    content: str
    timestamp: datetime

    class Config:
        orm_mode = True
