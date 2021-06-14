from flask import request
from flask_restx import Resource

from ..utilities.dto import  AuthorDto
from ..service.authorService import new_author, get_all_authors, get_author, save_changes
from typing import Dict, Tuple

api = AuthorDto.api
_author = AuthorDto.author

@api.route('/author')
class authorList(Resource):
    @api.doc('List of Authors')
    @api.marshal_list_with(_author, envelope='data')
    def get(self):
        """List all authors"""
        return get_all_authors

    @api.expect(_author, validate=True)
    @api.response(201, 'Author successfully added.')
    @api.doc('Add a new Author')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Author"""
        data = request.json
        return new_author(data=data)


@api.route('/author/<authorId>')
@api.param('authorId', 'The AuthorId of an Author')
@api.response(404, 'Author Not Found.')
class Author(Resource):
    @api.doc('get an author')
    @api.marshal_with(_author)
    def get(self, authorId):
        """get an author given their authorId"""
        author = get_author(authorId)
        if not author:
            api.abort(404)
        else:
            return author

    def delete(self, authorId):
        """delete an author given their authorId"""

