import uuid
from app.models.book import BookModel
from app.schemas.book import Book, BookCreate, BookUpdate
from pynamodb.exceptions import DoesNotExist, GetError, ScanError, PutError, UpdateError, DeleteError

class BookService:
    def get_book(self, book_id: str) -> Book | None:
        try:
            book_model = BookModel.get(hash_key=book_id)
            return Book(
                id=book_model.id,
                title=book_model.title,
                author=book_model.author,
                isbn=book_model.isbn,
                publication_year=book_model.publication_year,
                price=book_model.price,
                created_at=book_model.created_at,
                updated_at=book_model.updated_at
            )
        except DoesNotExist:
            return None
        except GetError as e:
            raise RuntimeError(f"Error fetching book: {str(e)}")

    def get_all_books(self) -> list[Book]:
        try:
            books = BookModel.scan()
            return [
                Book(
                    id=book.id,
                    title=book.title,
                    author=book.author,
                    isbn=book.isbn,
                    publication_year=book.publication_year,
                    price=book.price,
                    created_at=book.created_at,
                    updated_at=book.updated_at
                ) for book in books
            ]
        except ScanError as e:
            raise RuntimeError(f"Error scanning books: {str(e)}")

    def create_book(self, book: BookCreate) -> Book:
        try:
            book_model = BookModel(
                id=str(uuid.uuid4()),
                title=book.title,
                author=book.author,
                isbn=book.isbn,
                publication_year=book.publication_year,
                price=book.price
            )
            book_model.save()
            return Book(
                id=book_model.id,
                title=book_model.title,
                author=book_model.author,
                isbn=book_model.isbn,
                publication_year=book_model.publication_year,
                price=book_model.price,
                created_at=book_model.created_at,
                updated_at=book_model.updated_at
            )
        except PutError as e:
            raise RuntimeError(f"Error saving book: {str(e)}")

    def update_book(self, book_id: str, book_update: BookUpdate) -> Book | None:
        try:
            book_model = BookModel.get(hash_key=book_id)
            
            update_attrs = {}
            if book_update.title is not None:
                update_attrs['title'] = book_update.title
            if book_update.author is not None:
                update_attrs['author'] = book_update.author
            if book_update.isbn is not None:
                update_attrs['isbn'] = book_update.isbn
            if book_update.publication_year is not None:
                update_attrs['publication_year'] = book_update.publication_year
            if book_update.price is not None:
                update_attrs['price'] = book_update.price
                
            if update_attrs:
                for key, value in update_attrs.items():
                    setattr(book_model, key, value)
                book_model.save()
                
            return Book(
                id=book_model.id,
                title=book_model.title,
                author=book_model.author,
                isbn=book_model.isbn,
                publication_year=book_model.publication_year,
                price=book_model.price,
                created_at=book_model.created_at,
                updated_at=book_model.updated_at
            )
        except DoesNotExist:
            return None
        except (GetError, UpdateError) as e:
            raise RuntimeError(f"Error updating book: {str(e)}")

    def delete_book(self, book_id: str) -> bool:
        try:
            book_model = BookModel.get(hash_key=book_id)
            book_model.delete()
            return True
        except DoesNotExist:
            return False
        except (GetError, DeleteError) as e:
            raise RuntimeError(f"Error deleting book: {str(e)}") 