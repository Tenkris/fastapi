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
            # Validate phone number
            try:
                UserModel.validate_phone(user.tel)
            except ValueError as e:
                raise HTTPException(status_code=400, detail=str(e))

            # Create new user
            hashed_password = self.pwd_context.hash(user.password)
            
            new_user = UserModel(
                email=user.email,
                name=user.name,
                tel=user.tel,
                role=user.role,
                password=hashed_password,
                age = user.age,
                career=user.career,
                gender=user.gender.value if user.gender else None,
                hobbies=user.hobbies,
                reason=user.reason
            )
            new_user.save()
            
            # Create token
            token = await create_access_token({"sub": user.email, "role": user.role})
            
            return {"token": token, "user": UserResponse(**new_user.to_dict())}

    async def login(self, email: str, password: str):
        try:
            user = UserModel.get(email)
            
            if not self.pwd_context.verify(password, user.password):
                raise HTTPException(status_code=400, detail="Invalid credentials")
            
            # Create token
            token = await create_access_token({"sub": user.email, "role": user.role})
            
            # Send login confirmation email
            try:
                async with httpx.AsyncClient() as client:
                    await client.post(
                        f"{Config.EMAIL_SERVICE_URL}/login-confirmation",
                        json={"user_email": email},
                        headers={"Authorization": f"Bearer {token}"}
                    )
            except Exception as e:
                print(f"Failed to send login confirmation email: {e}")
            
            return {"token": token, "user": UserResponse(**user.to_dict())}
            
        except DoesNotExist:
            raise HTTPException(status_code=400, detail="Invalid credentials")
        except Exception as e:
            logger.log_user_error(
                user_email=email,
                error=e,
                function_name="login"
            )
            raise HTTPException(status_code=400, detail=str(e)) 
        
