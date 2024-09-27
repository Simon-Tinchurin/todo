from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Optional


# Also used for get endpoint
class TaskBase(BaseModel):
    datetime_to_do: datetime
    task_info: str

    class Config:
        from_attributes = True  # Enables ORM objects validation

# schema for PATCH requests 
class PartialUpdateTask(BaseModel):
    datetime_to_do: Optional[datetime] = None
    task_info: Optional[str] = None

    class Config:
        from_attributes = True

class Task(TaskBase):
    id: UUID
    created_at: datetime
    updated_at: datetime  

