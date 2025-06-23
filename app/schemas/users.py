from pydantic import BaseModel
from datetime import datetime
from .posts import PostResponse
from typing import Optional

class UserResponse(BaseModel):
    id: int
    username: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
