from fastapi import APIRouter, Depends, status
from app.services.question import QuestionService
from app.schemas.question import QuestionCreate, QuestionUpdate, QuestionResponse
from typing import List

router = APIRouter(
    prefix="/questions",
    tags=["questions"],
)

@router.post("", response_model=QuestionResponse, status_code=status.HTTP_201_CREATED)
async def create_question(
    question_data: QuestionCreate,
    question_service: QuestionService = Depends()
):
    """
    Create a new question
    """
    return await question_service.create_question(question_data)

@router.get("", response_model=List[QuestionResponse])
async def get_all_questions(
    question_service: QuestionService = Depends()
):
    """
    Get all questions
    """
    return await question_service.get_all_questions()

@router.get("/{question_id}", response_model=QuestionResponse)
async def get_question(
    question_id: str,
    question_service: QuestionService = Depends()
):
    """
    Get a specific question by ID
    """
    return await question_service.get_question(question_id)

@router.put("/{question_id}", response_model=QuestionResponse)
async def update_question(
    question_id: str,
    question_data: QuestionUpdate,
    question_service: QuestionService = Depends()
):
    """
    Update a question
    """
    return await question_service.update_question(question_id, question_data)

@router.delete("/{question_id}", status_code=status.HTTP_200_OK)
async def delete_question(
    question_id: str,
    question_service: QuestionService = Depends()
):
    """
    Delete a question
    """
    return await question_service.delete_question(question_id) 