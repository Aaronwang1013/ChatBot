from fastapi import FastAPI,Body

app = FastAPI() ## uvicorn is the webserver we use to start a FastAPI application


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]
## API endpoint
@app.get("/")
async def first_api():
    return {"message": "Hello Aaron"}
 
@app.get("/books/mybook")
async def read_all_books():
    return BOOKS

# if the params is not "mybook", this function will catch it
#path parameters
@app.get("/books/{book_title}")
async def read_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

# query parameters
@app.get("/books/")
async def read_category_by_query(category:str):
    books_to_return =[]
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return



@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author:str, category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# post request methods
@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)
    
# put request methods
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] == updated_book
            
            
# delete request methods
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
        

@app.get("/books/author/{book_author}")
async def get_specific_book(book_author:str):
    books_to_return = []
    for i in BOOKS:
        if i.get('author').casefold() == book_author.casefold():
            books_to_return.append(i)
    return books_to_return