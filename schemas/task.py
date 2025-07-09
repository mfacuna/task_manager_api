from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime, date
from enum import Enum

class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class TaskPriority(int, Enum):
    low = 1
    medium = 2
    high = 3

class TaskCreate(BaseModel):
    title: str = Field(..., max_length=100)
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.pending
    priority: TaskPriority = TaskPriority.medium
    due_date: Optional[date] = Field(None)

    @field_validator("due_date")
    @classmethod
    def no_past_due(cls, v: Optional[date]) -> Optional[date]:
        if v and v < date.today():
            raise ValueError("due_date cannot be in the past")
        return v
    
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[date] = Field(None)

    @field_validator("due_date")
    @classmethod
    def no_past_due(cls, v: Optional[date]) -> Optional[date]:
        if v and v < date.today():
            raise ValueError("due_date cannot be in the past")
        return v

class TaskResponse(TaskCreate):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None
