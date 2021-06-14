from app.main import db
from app.main.model.book import Book


def new_book(data):
    book = Book.query.filter_by(isbn=data['isbn']).first()
    if not book:
        newBook = book(
            isbnCode=data['isbnCode'],
            title=data['title'],
            language=data['language'],
            totalCopies=data['totalCopies'],
            availableCopies=data['availableCopies'],
            publicationYear=data['publicationYear'],
            categoryId=data['categoryId'],
            authorId=data['authorId'],
        )
        save_changes(newBook)
        response_object = {
            'status': 'success',
            'message': 'Successfully Added.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Book already in the system',
        }
        return response_object, 409


def get_all_books():
    return Book.query.all()


def get_book(isbnCode):
    return Book.query.filter_by(isbnCode=isbnCode).first()


def get_book_by_title(title):
    return Book.query.filter_by(title=title).first()

def delete_book(isbnCode):
    if get_book(isbnCode):
        return Book.query


def delete_book_title(title):


def save_changes(data):
    db.session.add(data)
    db.session.commit()
