from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Author

router = APIRouter(
    prefix="/top-authors",
    tags=["business"]
)

@router.get("/")
def get_top_authors(db: Session = Depends(get_db)):
    authors = db.query(Author).all()
    author_ratings = []
    for author in authors:
        if author.books:
            avg_rating = sum(book.rating for book in author.books) / len(author.books)
            author_ratings.append({"author": author.name, "avg_rating": avg_rating})
    top = sorted(author_ratings, key=lambda x: x["avg_rating"], reverse=True)[:3]
    return top
