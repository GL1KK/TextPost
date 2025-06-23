from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostResponse(BaseModel):
    id: int
    title: str
    data: str
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class PostUpdate(BaseModel):
    title: Optional[str] = None
    data: Optional[str] = None

    class Config:
        from_attributes = True