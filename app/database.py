from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String
from config import settings
import asyncio
from typing import Annotated

engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=False,
)

session = async_sessionmaker(engine)

username_20 = Annotated[str, 20]

class Base(DeclarativeBase):    
    type_annotation_map = {
        username_20: String(20)
    }


async def get_db() -> AsyncSession:
    async with session() as sn:
        try:
            yield sn
        except Exception:
            await sn.rollback()
            raise
        finally:
            await sn.close()