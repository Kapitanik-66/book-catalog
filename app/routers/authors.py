from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/authors",
    tags=["authors"]
)

@router.post("/", response_model=schemas.AuthorOut)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_author = models.Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

@router.get("/", response_model=list[schemas.AuthorOut])
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Author).offset(skip).limit(limit).all()
