from fastapi import APIRouter, Depends, HTTPException
from app.services.user import UserService
from app.schemas.user import UserResponse, UserUpdate
from app.middleware.auth import verify_token, check_permissions
from typing import List

router = APIRouter()
user_service = UserService()

@router.get("/me", response_model=dict)
async def get_current_user(payload: dict = Depends(verify_token)):
    try:
        user = await user_service.get_user(payload["sub"])
        return {"status": "success", "data": user}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=dict)
async def get_all_users(payload: dict = Depends(check_permissions(["admin"]))):
    try:
        users = await user_service.get_all_users()
        return {"status": "success", "data": users}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/update", response_model=dict)
async def update_user(
    updated_fields: UserUpdate,
    payload: dict = Depends(verify_token)
) -> dict:
    try:
        result = await user_service.update_user(payload["sub"], updated_fields)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))