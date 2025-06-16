from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String
from .config import settings
import asyncio
from typing import Annotated

engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=False,
)

session = async_sessionmaker(engine)

username = Annotated[str, 20]

class Base(DeclarativeBase):    
    type_annotation_map = {
        username: String(20)
    }