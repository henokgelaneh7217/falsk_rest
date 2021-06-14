import uuid
import datetime

from app.main import db
from app.main.model.student import Student
from typing import Dict, Tuple, Any


def new_student(data: Dict[Any, Any]) -> Tuple[Dict[Any, Any], int]:
    student = Student.query.filter_by(email=data['email']).first()
    if not student:
        newStudent = Student(
            studentId=uuid.uuid4(),
            studentName=data['studentName'],
            email=data['email'],
            sex=data['sex'],
            dateofBirth=data['dateofBirth'],
            department=data['department'],
            registered_on=datetime.datetime.utcnow(),
            password=data['password']
        )
        save_changes(newStudent)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Email already taken, please log in',
        }
        return response_object, 409


def get_all_users():
    return Student.query.all()


def get_user(studentId):
    return Student.query.filter_by(studentId=studentId).first()


def get_user_by_email(email):
    return Student.query.filter_by(email=email).first()


def generate_token(student: Student) -> Tuple[Dict[Any, Any], int]:
    try:
        token = Student.token_encode(Student.studentId)
        response = {
            'status': 'success',
            'message': 'Registered',
            'authorization': token.decode()
        }
        return response, 201
    except Exception as e:
        response = {
            'status': 'failure',
            'message': 'error'
        }


def save_changes(data):
    db.session.add(data)
    db.session.commit()
