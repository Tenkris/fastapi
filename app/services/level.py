from fastapi import HTTPException
from pynamodb.exceptions import DoesNotExist
from app.models.level import LevelModel
from app.models.question import QuestionModel
from app.schemas.level import LevelCreate, LevelUpdate, LevelResponse
from typing import List, Optional
from datetime import datetime, timezone

class LevelService:
    async def create_level(self, level_data: LevelCreate) -> LevelResponse:
        """
        Create a new level
        """
        try:
            # Check if level already exists
            try:
                existing_level = LevelModel.get(level_data.level)
                raise HTTPException(status_code=400, detail=f"Level {level_data.level} already exists")
            except DoesNotExist:
                pass
            
            # Validate question_ids if provided
            if level_data.question_ids:
                for question_id in level_data.question_ids:
                    try:
                        QuestionModel.get(question_id)
                    except DoesNotExist:
                        raise HTTPException(status_code=400, detail=f"Question with id {question_id} does not exist")
            
            level = LevelModel(
                level=level_data.level,
                boss_name=level_data.boss_name,
                boss_image_s3=level_data.boss_image_s3,
                boss_hp=level_data.boss_hp,
                boss_attack=level_data.boss_attack,
                question_ids=level_data.question_ids
            )
            level.save()
            return LevelResponse(**level.to_dict())
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error creating level: {str(e)}")

    async def get_all_levels(self) -> List[LevelResponse]:
        """
        Get all levels
        """
        try:
            levels = LevelModel.scan()
            return [LevelResponse(**level.to_dict()) for level in levels]
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching levels: {str(e)}")

    async def get_level(self, level_id: int) -> LevelResponse:
        """
        Get a level by ID
        """
        try:
            level = LevelModel.get(level_id)
            return LevelResponse(**level.to_dict())
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Level not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching level: {str(e)}")
    
    async def update_level(self, level_id: int, level_data: LevelUpdate) -> LevelResponse:
        """
        Update level fields
        """
        try:
            level = LevelModel.get(level_id)
            
            # Get the updated fields only
            update_data = level_data.dict(exclude_unset=True, exclude_none=True)
            
            # Validate question_ids if provided
            if 'question_ids' in update_data and update_data['question_ids']:
                for question_id in update_data['question_ids']:
                    try:
                        QuestionModel.get(question_id)
                    except DoesNotExist:
                        raise HTTPException(status_code=400, detail=f"Question with id {question_id} does not exist")
            
            # Update level fields
            if 'boss_name' in update_data and update_data['boss_name']:
                level.boss_name = update_data['boss_name']
                
            if 'boss_image_s3' in update_data:
                level.boss_image_s3 = update_data['boss_image_s3']
                
            if 'boss_hp' in update_data and update_data['boss_hp'] is not None:
                level.boss_hp = update_data['boss_hp']
                
            if 'boss_attack' in update_data and update_data['boss_attack'] is not None:
                level.boss_attack = update_data['boss_attack']
                
            if 'question_ids' in update_data and update_data['question_ids'] is not None:
                level.question_ids = update_data['question_ids']
            
            # Update the updated_at field
            level.updated_at = datetime.now(timezone.utc)
            
            level.save()
            return LevelResponse(**level.to_dict())
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Level not found")
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error updating level: {str(e)}")
            
    async def delete_level(self, level_id: int) -> dict:
        """
        Delete a level
        """
        try:
            level = LevelModel.get(level_id)
            level.delete()
            return {"success": True, "message": "Level deleted successfully"}
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Level not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error deleting level: {str(e)}")
            
    async def add_question_to_level(self, level_id: int, question_id: str) -> LevelResponse:
        """
        Add a question to a level
        """
        try:
            level = LevelModel.get(level_id)
            
            # Check if question exists
            try:
                QuestionModel.get(question_id)
            except DoesNotExist:
                raise HTTPException(status_code=404, detail=f"Question with id {question_id} not found")
            
            # Check if question already in level
            if question_id in level.question_ids:
                raise HTTPException(status_code=400, detail=f"Question already in level {level_id}")
                
            # Add question to level
            level.question_ids.append(question_id)
            level.updated_at = datetime.now(timezone.utc)
            level.save()
            
            return LevelResponse(**level.to_dict())
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Level not found")
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error adding question to level: {str(e)}")
            
    async def remove_question_from_level(self, level_id: int, question_id: str) -> LevelResponse:
        """
        Remove a question from a level
        """
        try:
            level = LevelModel.get(level_id)
            
            # Check if question in level
            if question_id not in level.question_ids:
                raise HTTPException(status_code=400, detail=f"Question not in level {level_id}")
                
            # Remove question from level
            level.question_ids.remove(question_id)
            level.updated_at = datetime.now(timezone.utc)
            level.save()
            
            return LevelResponse(**level.to_dict())
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Level not found")
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error removing question from level: {str(e)}") 