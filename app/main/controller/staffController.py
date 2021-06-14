from flask import request
from flask_restx import Resource
from ..utilities.dto import StaffDto
from ..service.staffService import get_all_staffs, get_staff,get_staff_by_title, new_staff
from typing import Dict, Tuple

api = StaffDto.api
_staff = StaffDto.staff

@api.route('/staff')
class staffList(Resource):
    @api.doc('List of Staff')
    @api.marshal_list_with(_staff,envelope='data')
    def get(self):
        """List all registered staff"""
        return get_all_staffs()
    @api.expect(_staff,validate=True)
    @api.response(201,'Staff successfully loaded')
    @api.doc('Add a new staff')
    def post(self) -> Tuple[Dict[str,str], int]:
        """create a staff"""
        data = request.json
        return new_staff()


@api.route('/staff/<privateId>')
@api.param('privateId', 'The private id of staff')
@api.response(404, 'staff not found.')
class Staff(Resource):
    @api.doc('get a staff')
    @api.marshal_with(_staff)
    def get(self, privateId):
        staff = get_staff(privateId)
        if not staff:
            api.abort(404)
        else:
            return staff

    def delete(self, privateId):
        """delete a staff given its privateid"""

@api.route('/staff/<staffName>')
@api.param('staffName', 'The name for staff')
@api.response(404, 'staff not found.')
class StaffName(Resource):
    @api.doc('get a staff by using staffName')
    @api.marshal_with(_staff)
    def get(self, title):
        """get a user given its identifier"""
        staff = get_staff(title)
        if not staff:
            api.abort(404)
        else:
            return staff
