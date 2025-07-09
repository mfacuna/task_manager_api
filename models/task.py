# models/task.py
from datetime import datetime
from typing import Optional
from beanie import Document

class TaskModel(Document):
    title: str
    description: Optional[str] = None
    status: str
    priority: int
    due_date: Optional[datetime] = None
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()

    class Settings:
        name = "tasks"

    class Config:
        schema_extra = {
            "example": {
                "title": "Comprar leche",
                "description": "Leche, pan y huevos",
                "status": "pending",
                "priority": 2,
                "due_date": "2025-07-10T00:00:00Z"
            }
        }
