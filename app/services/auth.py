from fastapi import HTTPException
from passlib.context import CryptContext
import httpx
from app.models.user import UserModel
from app.schemas.user import UserCreate, UserResponse 
from app.middleware.auth import create_access_token
from app.utils.config import Config
from pynamodb.exceptions import DoesNotExist



class AuthService:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def register(self, user: UserCreate):
        try:
            # Check if user exists
            UserModel.get(user.email)
            raise HTTPException(status_code=409, detail="Email already registered")
        except DoesNotExist:
            # Create new user
            hashed_password = self.pwd_context.hash(user.password)
            
            new_user = UserModel(
                email=user.email,
                name=user.name,
                password=hashed_password,
                level_id=user.level_id if user.level_id else 1,
                user_image=user.user_image,
                attack=user.attack if user.attack else 10.0,
                defense=user.defense if user.defense else 10.0,
                speed=user.speed if user.speed else 10.0,
                critical=user.critical if user.critical else 5.0,
                hp=user.hp if user.hp else 100.0
            )
            new_user.save()
            
            # Create token
            token = await create_access_token({"sub": user.email})
            
            return {"token": token, "user": UserResponse(**new_user.to_dict())}

    async def login(self, email: str, password: str):
        try:
            user = UserModel.get(email)
            
            if not self.pwd_context.verify(password, user.password):
                raise HTTPException(status_code=400, detail="Invalid credentials")
            
            # Create token
            token = await create_access_token({"sub": user.email})
            return {"token": token, "user": UserResponse(**user.to_dict())}
            
        except DoesNotExist:
            raise HTTPException(status_code=400, detail="Invalid credentials")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e)) 
        
