import uuid
import datetime

from app.main import db
from app.main.model.borrower import Borrower


def new_borrower(data):
    borrower = Borrower.query.filter_by(email=data['email']).first()
    if not borrower:
        newBorrower = Borrower(
            # borrowerId=uuid.uuid4(),
            # bookId
            # dateofBorrow = datetime.datetime.utcnow(),
            # borrowedTo
            # actualReturnDate

        )
        save_changes(newBorrower)
        response_object = {
            'status': 'success',
            'message': 'Successfully Added.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Borrow quota reached.',
        }
        return response_object, 409


def get_all_users():
    return Borrower.query.all()


def get_user(borrowerId):
    return Borrower.query.filter_by(borrowerId=borrowerId).first()


def get_user_by_email(email):
    return Borrower.query.filter_by(email=email).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
