from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
app=FastAPI()

class Book():
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self,id,title,author,description,rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date= published_date


class BookRequest(BaseModel):
    #id: Optional[int]=None
    id: Optional[int]= Field(description="ID is not needed on create", default= None)
    title:str = Field(min_length=3)
    author:str =Field(min_length=1)
    description:str = Field(min_length=1, max_length=100)
    rating:int =Field(gt=0,lt=6)
    published_date:int =Field(gt=1999, lt=2031)
    
    model_config={
        "json_schema_extra": {
            "example": {
                "title":"A new book",
                "author":"ABC",
                "description":"good book",
                "rating":1,
                "published_date":2030
            }
        }
    }

BOOKS=[
    Book(1,'Computer Science Pro','Coding', 'A Very nice book', 5,2029),
    Book(2,'Machine Learning Basics', 'AI', 'Great foundation for beginners', 4, 2028),
    Book(3,'Python in Depth', 'Programming', 'Covers advanced Python concepts', 5, 2027),
    Book(4,'Django for APIs', 'Web Development', 'Practical API building guide', 2, 2026),
    Book(5,'Clean Code', 'Software Engineering', 'Principles of coding style', 3, 2029),
    Book(6,'Fluent Python', 'Programming', 'Best practices', 2, 2030)
]
@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id: int= Path(gt=0)):
    for book in BOOKS:
        if book.id== book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/books/")
async def read_book_by_rating(book_rating: int):
    books_to_return= []
    for book in BOOKS:
        if book.rating== book_rating:
            books_to_return.append(book)
    return books_to_return

@app.post("/create-book")
async def create_book(book_request:BookRequest):
    new_book=Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book:Book):
    if len(BOOKS)>0:
        book.id=BOOKS[-1].id+1
    else:
        book.id=1
    return book


@app.put("/books/update_book")
async def update_book(book:BookRequest):
    book_changed=False
    for i in range (len(BOOKS)):
        if BOOKS[i].id== book.id:
            BOOKS[i]= book
            book_changed=True
    if not book_changed:
        raise HTTPException(status_code=404,detail='Item not found')
       

@app.delete("/books/{book_id}")
async def delete_book(book_id:int):
    book_changed= False
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book_id:
            BOOKS.pop(i)
            book_changed=True
            break 
    if not book_changed:
        raise HTTPException(status_code=404,detail='Item not found')          