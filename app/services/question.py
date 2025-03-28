from fastapi import HTTPException
from pynamodb.exceptions import DoesNotExist
from app.models.question import QuestionModel, QuestionType
from app.schemas.question import QuestionCreate, QuestionUpdate, QuestionResponse
from typing import List, Optional
import uuid
from datetime import datetime, timezone

class QuestionService:
    async def create_question(self, question_data: QuestionCreate) -> QuestionResponse:
        """
        Create a new question
        """
        try:
            question_id = str(uuid.uuid4())
            question = QuestionModel(
                question_id=question_id,
                question=question_data.question,
                type=question_data.type.value,
                time_countdown=question_data.time_countdown,
                answer=question_data.answer
            )
            question.save()
            return QuestionResponse(**question.to_dict())
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error creating question: {str(e)}")

    async def get_all_questions(self) -> List[QuestionResponse]:
        """
        Get all questions
        """
        try:
            questions = QuestionModel.scan()
            return [QuestionResponse(**question.to_dict()) for question in questions]
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching questions: {str(e)}")

    async def get_question(self, question_id: str) -> QuestionResponse:
        """
        Get a question by ID
        """
        try:
            question = QuestionModel.get(question_id)
            return QuestionResponse(**question.to_dict())
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Question not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching question: {str(e)}")
    
    async def update_question(self, question_id: str, question_data: QuestionUpdate) -> QuestionResponse:
        """
        Update question fields
        """
        try:
            question = QuestionModel.get(question_id)
            
            # Get the updated fields only
            update_data = question_data.dict(exclude_unset=True)
            
            # Update question fields
            if 'question' in update_data and update_data['question']:
                question.question = update_data['question']
                
            if 'type' in update_data and update_data['type']:
                question.type = update_data['type'].value
                
            if 'time_countdown' in update_data and update_data['time_countdown'] is not None:
                question.time_countdown = update_data['time_countdown']
                
            if 'answer' in update_data and update_data['answer']:
                question.answer = update_data['answer']
            
            # Update the updated_at field
            question.updated_at = datetime.now(timezone.utc)
            
            question.save()
            return QuestionResponse(**question.to_dict())
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Question not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error updating question: {str(e)}")
            
    async def delete_question(self, question_id: str) -> dict:
        """
        Delete a question
        """
        try:
            question = QuestionModel.get(question_id)
            question.delete()
            return {"success": True, "message": "Question deleted successfully"}
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Question not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error deleting question: {str(e)}") 