from datetime import datetime, timezone

from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import uuid

Base = declarative_base()


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass


class Message(Base):
    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    sender_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    receiver_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))

    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])
