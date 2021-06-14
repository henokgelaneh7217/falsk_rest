from flask import request
from flask_restx import Resource

from ..utilities.dto import studentDto
from ..service.studentService import get_all_users, get_user, new_student
from typing import Dict, Tuple

api = studentDto.api
_student = studentDto.student


@api.route('/student')
class StudentList(Resource):
    @api.doc('List of Users')
    @api.marshal_list_with(_student, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(_student, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new student"""
        data = request.json
        return new_student(data=data)


@api.route('/student/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class Student(Resource):
    @api.doc('get a user')
    @api.marshal_with(_student)
    def get(self, public_id):
        """get a student given identifier"""
        user = get_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
