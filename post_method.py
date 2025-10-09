from fastapi import Body, FastAPI # Imports the FastAPI class so we can create a FastAPI application

app = FastAPI() # Creates a FastAPI application instance — this is the main entry point of the API
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
    books_to_return=[] # Create an empty list to store matching books
    for book in BOOKS: # Loop through each book in the BOOKS list
        if book.get('category').casefold()==category.casefold():  # Compare book's category with given category (case-insensitive)
            books_to_return.append(book)  # If category matches, add book to result list
    return books_to_return # Return the list of matching books

@app.get("/books/{book_author}/") # http://127.0.0.1:8000/path_param/author%20four/?category=science 
# Define a GET endpoint with a path parameter 'book_author'
async def read_author_category_by_query(book_author: str , category: str):
    books_to_return=[] # Create an empty list to store books matching the author and category
    for book in BOOKS: # Loop through each book in the BOOKS list
        # Check if book's author matches given author (case-insensitive)
        # AND if book's category matches given category (case-insensitive)
        if book.get('author').casefold()==book_author.casefold() and book.get('category').casefold()==category.casefold():  
            books_to_return.append(book) # If both conditions match, add this book to the results list 
    return books_to_return # Return the list of matching books

# This FastAPI decorator specifies that when a POST request is made to this URL,
#    the function below will be executed.
@app.post("/path_param/create_book")

# This line defines a function named create_book.
#    'async def' means this is an asynchronous function, allowing fast/efficient co

@app.post("/path_param/create_book")

# This line defines a function named create_book.
#    'async def' means this is an asynchronous function, allowing fast/efficient co

async def create_book(new_book: dict = Body()):

# new_book is an argument meant to come from the request body

# Here, the new book is being added to the global BOOKS list.
    BOOKS.append(new_book) # This adds the new book to the list.
    return {"message": "Book created", "book": new_book}

# This decorator defines a PUT HTTP endpoint at path "path_param/update_book"
@app.put("path_param/update_book")
# An asynchronous function to handle the update book request
async def update_book(updated_book=Body()):
    # Loop through the list of BOOKS by index
    for i in range(len(BOOKS)):
                # Check if the title of the current book matches the title of the incoming updated book (case-insensitive)

        if BOOKS[i].get('title').casefold()==updated_book.get('title').casefold():
             # Replace the matched book with the updated book data
            BOOKS[i]=updated_book