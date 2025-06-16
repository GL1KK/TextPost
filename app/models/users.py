from ..database import Base, username
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import text, String
from typing import Annotated
from datetime import datetime

intpk = Annotated[int, mapped_column(primary_key=True)]
creared_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow)]

class Users(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    username: Mapped[username]
    password: Mapped[str] = mapped_column(String(255))
