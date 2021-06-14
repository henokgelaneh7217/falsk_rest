from flask import request
from flask_restx import Resource

from ..utilities.dto import categoryDto
from ..service.categoryService import new_category,get_all_categories,get_category,save_changes
from typing import Dict, Tuple

api = categoryDto.api
_category = categoryDto.category

@api.route('/category')
class categoryList(Resource):
    @api.doc('List of categorys')
    @api.marshal_list_with(_category, envelope='data')
    def get(self):
        """List all categories"""
        return get_all_categories

    @api.expect(_category, validate=True)
    @api.response(201, 'category successfully added.')
    @api.doc('Add a new category')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new category"""
        data = request.json
        return new_category(data=data)


@api.route('/category/<categoryId>')
@api.param('categoryId', 'The categoryId of a category')
@api.response(404, 'category Not Found.')
class category(Resource):
    @api.doc('get a category')
    @api.marshal_with(_category)
    def get(self, categoryId):
        """get a category given its categoryId"""
        category = get_category(categoryId)
        if not category:
            api.abort(404)
        else:
            return category

    def delete(self, categoryId):
        """delete a category given its categoryId"""
