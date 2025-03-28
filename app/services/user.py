from fastapi import HTTPException
from pynamodb.exceptions import DoesNotExist
from app.models.user import UserModel
from app.schemas.user import UserResponse, UserUpdate
from typing import List

class UserService:
    async def get_all_users(self) -> List[UserResponse]:
        """
        Get all users (admin only)
        """
        try:
            users = UserModel.scan()
            return [UserResponse(**user.to_dict()) for user in users]
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching users: {str(e)}")

    async def get_user(self, email: str):
        try:
            user = UserModel.get(email)
            return UserResponse(**user.to_dict())
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="User not found")
        
    async def update_user(self, user_email: str, updated_fields: UserUpdate) -> UserResponse:
        """
        Update user profile fields
        """
        try:
            user = UserModel.get(user_email)
            
            # Update only provided fields
            for field, value in updated_fields.dict(exclude_unset=True).items():
                if hasattr(user, field):
                    if field == "gender" and value:
                        value = value.value if hasattr(value, 'value') else value
                    setattr(user, field, value)
            
            user.save()
            return UserResponse(**user.to_dict())
            
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="User not found")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))