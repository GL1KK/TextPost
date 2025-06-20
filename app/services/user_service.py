from models.users import Users
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text, insert, select, and_, cast
from sqlalchemy.orm import selectinload, joinedload
from datetime import datetime
from database import Base, engine, session

class UserServies:
    async def get_profile(self, user_id: str):
        async with session() as sn:
            query = (
                select(Users)
                .filter(Users.id == int(user_id))
            )

            res = await sn.execute(query)
            user = res.scalar_one()
            return user