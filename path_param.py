from fastapi import FastAPI

app = FastAPI()
# Example data list (Books data)
BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/")  # Root route: responds to "/"# http://127.0.0.1:8000
async def root():
    # Return a welcome message at the root URL
    return {"message": "Welcome to the API"}

@app.get("/path_param") # http://127.0.0.1:8000/path_param
async def read_all_books():
    # Return all books
    return BOOKS
# -------------------------------
# Static route (no path parameters)
# -------------------------------

# When user visits /path_param/mybook
# this will return a fixed book title

@app.get("/path_param/mybook") # http://127.0.0.1:8000/path_param/mybook
async def read_book():
    return {'book title': 'My Favorite Book'}

@app.get("/path_param/{dynamic_param}") # http://127.0.0.1:8000/path_param/pop
async def read_book(dynamic_param: str):
    # Return the dynamic parameter received in path
    return {'dynamic_param': dynamic_param}
# -------------------------------
# Path Parameter Example in FastAPI
# -------------------------------

# When the user requests /path_param/<book_title>,
# this route will be triggered
@app.get("/path_param/{book_title}") # http://127.0.0.1:8000/path_param/title one
async def read_book(book_title:str):
     # Loop through each book in the BOOKS list
    for book in BOOKS:
        # Use casefold() for case-insensitive comparison
        # e.g. "harrypotter" and "HARRYPOTTER" will match
        if book.get('title').casefold()==book_title.casefold():
             # If title matches, return the whole book data
            return book
    # If no match is found, return a message
    return {"message": "Book not found"}
@app.get("/books/") # http://127.0.0.1:8000/books/?category=math
async def read_book(category: str):
    books_to_return=[]
    for book in BOOKS:
        if book.get('category').casefold()==category.casefold():
            books_to_return.append(book)
    return books_to_return