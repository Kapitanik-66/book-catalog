from fastapi import FastAPI
from .database import Base, engine
from .routers import users, authors, books, business

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(authors.router)
app.include_router(books.router)
app.include_router(business.router)

@app.get("/")
def root():
    return {"message": "Book Catalog API"}
