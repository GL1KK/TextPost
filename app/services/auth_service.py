from models.users import Users
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text, insert, select, and_, cast
from sqlalchemy.orm import selectinload, joinedload
from datetime import datetime
from database import Base, engine, session
from utils.security import Security
from fastapi import HTTPException


class AuthService:
    def __init__(self):
        self.__security = Security() 

    async def register_user(self, username: str, password: str):
        async with session() as sn:
            try:
                hashed_password = self.__security.hash_password(password=password)
                user = (
                    Users(username=username, password=hashed_password)
                    )
                sn.add(user)
                await sn.commit()
                await sn.refresh(user)
                return user
            except IntegrityError:
                await sn.rollback()
                raise HTTPException(status_code=409, detail="Username is not avaible!")
    
    async def login_user(self, username: str, password: str):
        async with session() as sn:
            try:
                query = (
                    select(Users)
                    .filter(username=username)
                )
                res = await sn.execute(query)
                user = res.scalar_one_or_none()
                if user is not None:
                    hashed_password = user.password
                    check_data = self.__security.verify_password(hashed_pwd=hashed_password,password=password)
                    if check_data:
                        return user
                    else:
                        raise HTTPException(status_code=409, detail="Username or password incorrect! Try again!")
                else:
                    raise HTTPException(status_code=403, detail="Npt")
            except Exception as e:
                raise HTTPException(status_code=409, detail="Username or password incorrect! Try again!")
                
                