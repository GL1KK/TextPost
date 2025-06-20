from database import Base, username_20
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import text, String
from typing import Annotated
from datetime import datetime

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow)]

class Users(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    username: Mapped[username_20] = mapped_column(unique=True)
    password: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    posts = relationship(
        "Posts",
        back_populates="user",
    )
