from fastapi import APIRouter, HTTPException, Query
from app.schemas.book import Book, BookCreate, BookUpdate
from app.services.books import BookService

router = APIRouter()
book_service = BookService()

@router.get("/{book_id}", response_model=Book)
async def read_book(book_id: str) -> Book:
    try:
        book = book_service.get_book(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=list[Book])
async def read_all_books() -> list[Book]:
    try:
        return book_service.get_all_books()
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", response_model=Book, status_code=201)
async def create_book(book: BookCreate) -> Book:
    try:
        return book_service.create_book(book)
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{book_id}", response_model=Book)
async def update_book(book_id: str, book: BookUpdate) -> Book:
    try:
        updated_book = book_service.update_book(book_id, book)
        if not updated_book:
            raise HTTPException(status_code=404, detail="Book not found")
        return updated_book
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: str) -> None:
    try:
        deleted = book_service.delete_book(book_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Book not found")
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 