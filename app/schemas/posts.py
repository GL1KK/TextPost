from pydantic import BaseModel
from datetime import datetime


class PostResponse(BaseModel):
    id: int
    title: str
    data: str
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True