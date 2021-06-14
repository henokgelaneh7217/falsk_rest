import uuid
import datetime
from app.main import db
from app.main.model.staff import Staff


def new_staff(data):
    staff = Staff.query.filter_by(isbn=data['isbn']).first()
    if not staff:
        newstaff = staff(
            staffId=uuid.uuid4(),
            staffName=data['staffName'],
            registered_on=datetime.datetime.utcnow(),
            password=data['password']
        )
        save_changes(newstaff)
        response_object = {
            'status': 'success',
            'message': 'Successfully Registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'staff already in the system',
        }
        return response_object, 409


def get_all_staffs():
    return Staff.query.all()


def get_staff(isbnCode):
    return Staff.query.filter_by(isbnCode=isbnCode).first()


def get_staff_by_title(title):
    return Staff.query.filter_by(title=title).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
