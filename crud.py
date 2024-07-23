from sqlalchemy.orm import Session
from db import models
import schemas


def get_all_books(db: Session):
    return db.query(models.Book).all()


def retrieve_book(db: Session, book_id: int):
    if book_id:
        return db.query(models.Book).filter(models.Book.id == book_id).first()


def create_book(db: Session, book: schemas.BookBase):
    book = models.Book(
        title=book.title,
        summary=book.summary,
        author_id=book.author_id,
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book_id: int):
    try:
        book = db.query(models.Book).filter(models.Book.id == book_id).first()
        db.delete(book)
        db.commit()
        return {"message": "Book has been deleted successfully."}
    except Exception as e:
        db.rollback()
        raise {"message": str(e)}


def get_all_authors(db: Session):
    return db.query(models.Author).all()


def retrieve_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def create_author(db: Session, author: schemas.AuthorBase):
    author = models.Author(
        name=author.name,
        bio=author.bio,
    )
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


def delete_author(db: Session, author_id: int):
    try:
        author = db.query(models.Author).filter(models.Author.id == author_id).first()
        db.delete(author)
        db.commit()
        return {"message": "Author has been deleted successfully."}
    except Exception as e:
        db.rollback()
        raise {"message": str(e)}
