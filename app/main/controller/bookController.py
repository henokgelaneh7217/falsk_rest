from flask import request
from flask_restx import Resource

from ..utilities.dto import bookDto
from ..service.bookService import get_all_books, get_book, get_book_by_title, new_book
from typing import Dict, Tuple

api = bookDto.api
_book = bookDto.book


@api.route('/book')
class bookList(Resource):
    @api.doc('List of Books')
    @api.marshal_list_with(_book, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_books()

    @api.expect(_book, validate=True)
    @api.response(201, 'Book successfully added.')
    @api.doc('Add a new book')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new User """
        data = request.json
        return new_book(data=data)


@api.route('/book/<isbnCode>')
@api.param('isbnCode', 'The ISBN Code for book')
@api.response(404, 'Book not found.')
class Book(Resource):
    @api.doc('get a book')
    @api.marshal_with(_book)
    def get(self, isbnCode):
        """get a book given its isbn"""
        book = get_book(isbnCode)
        if not book:
            api.abort(404)
        else:
            return book

    def delete(self, isbnCode):
        """delete a book given its isbn"""


@api.route('/book/<title>')
@api.param('title', 'The title for book')
@api.response(404, 'Book not found.')
class BookName(Resource):
    @api.doc('get a book using title')
    @api.marshal_with(_book)
    def get(self, title):
        """get a user given its identifier"""
        book = get_book(title)
        if not book:
            api.abort(404)
        else:
            return book
