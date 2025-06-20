from database import Base, username_20
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import text, String, ForeignKey
from typing import Annotated
from datetime import datetime

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow)]

class Posts(Base):
    __tablename__ = "posts"

    id: Mapped[intpk]
    title: Mapped[str]
    data: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship(
        "Users",
        back_populates="posts",
    )