from fastapi import Body, FastAPI
from pydantic import BaseModel
app=FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self,id,title,author,description,rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

BOOKS=[
    Book(1,'Computer Science Pro','Coding', 'A Very nice book', 5),
    Book(2,'Machine Learning Basics', 'AI', 'Great foundation for beginners', 4),
    Book(3,'Python in Depth', 'Programming', 'Covers advanced Python concepts', 5),
    Book(4,'Django for APIs', 'Web Development', 'Practical API building guide', 2),
    Book(5,'Clean Code', 'Software Engineering', 'Principles of coding style', 3),
    Book(6,'Fluent Python', 'Programming', 'Best practices', 2)
]

@app.get("/books")
async def read_all_books():
    return BOOKS


@app.put("/create-book")
async def create_book(book_request=Body()):
    BOOKS.append(book_request)