
from flask import request
from flask_restx import Resource
from ..utilities.dto import BorrowDto
from ..service.borrowerService import get_all_users,get_user,get_user_by_email, new_borrower
from typing import Dict,Tuple

api= BorrowDto.api
_borrower=BorrowDto.borrower

@api.route('/borrow')
class borrowerList(Resource):
    @api.doc('List of Borrowers')
    @api.marshal_list_with(_borrower, envelope='data')
    def get(self):
        return get_all_users()

    @api.expect(_borrower,validate=True)
    @api.response(201,'Book successfully borrowed.')
    @api.doc('borrow a book')
    def post(self) -> Tuple[Dict[str,str],int]:
        data = request.json
        return new_borrower(data=data)

@api.route('/borrow/<borrowerId>')
@api.param('borrowerId','id of the user that borrowed a book')
@api.response(404,'borrower not found')
class Borrower(Resource):
    @api.doc('get a borrower')
    @api.marshal_with(_borrower)
    def get(self, borrowerId):
        borrower = get_user(borrowerId)
        if not borrower:
            api.abort(404)
        else:
            return borrower

    def delete(self,borrowerId):
        """delete a a user with """ 
