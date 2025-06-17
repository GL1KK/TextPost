from fastapi import APIRouter
from services.auth_service import AuthService
from schemas.users import UserResponse

class AuthRouter:
    def __init__(self):
        self.router = APIRouter(tags=["Auth"])
        self.__auth_service = AuthService()
        self._setup_routers()

    def _setup_routers(self):
        self.router.post("/register", response_model=UserResponse)(self.register_user)
        self.router.get("/login", response_model=UserResponse)(self.login_user)
    
    async def register_user(self, username: str, password: str):
        user = await self.__auth_service.register_user(username=username, password=password)
        return user

    async def login_user(self, username: str, password: str):
        user = await self.__auth_service.login_user(username=username, password=password)
        return user
        
    