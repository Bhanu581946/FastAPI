class Book:
    def __init__(self, book_id, title):
        print("id of self =", id(self))
        self.book_id = book_id
        self.title = title

b1 = Book(1, 'CSS')
print("id of b1   =", id(b1))

       