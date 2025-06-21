from fastapi import APIRouter, Depends
from services.user_service import UserServies
from schemas.users import UserResponse
from utils.security import auth

class UserRouter:
    def __init__(self):
        self.router = APIRouter(tags=["User"])
        self.__user_sesrvies = UserServies()
        self._setup_routers()

    def _setup_routers(self):
        self.router.get("/me", response_model=UserResponse)(self.profile)
    
    async def profile(self, user_id: str = Depends(auth.access_token_required)):
        user = await self.__user_sesrvies.get_profile(user_id=user_id.sub)
        return user