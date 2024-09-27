from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID as UUIDType
from sqlalchemy.sql import func
from .database import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(UUIDType(as_uuid=True), primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    datetime_to_do = Column(DateTime(timezone=True), nullable=False)
    task_info = Column(String, index=True, nullable=False)
