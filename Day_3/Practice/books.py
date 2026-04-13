from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn


app = FastAPI()

class Book(BaseModel):
    title: str
    author: str | None = None

books_db = {}
book_id = 0

@app.post('/books')
def create_book(book: Book):
    global book_id 
    book_id += 1
    books_db[book_id] = book
    return {
        "message": 'Book added',
        "content": book
        }


@app.get('/books')
def show_all_books():
    return books_db


@app.get('/books/{book_id}')
def get_book_by_id(book_id: int):
    try:
        return books_db[book_id]
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} does not exist")

@app.put('/books/{book_id}')
def update_book_by_id(book_id: int, book=Body()):
    books_db[book_id] = book
    try:
        return {
            "message": f'Updated book. Book id: {book_id}',
            "content": {books_db[book_id]}
        }
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} does not exist")


@app.delete('/books/{book_id}')
def delete_book_by_id(book_id: int):
    try:
        return {
            "message": 'Deleted book',
            "content": books_db.pop(book_id)
        }
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} does not exist")


if __name__ == '__main__':
    uvicorn.run('books:app', reload=True)