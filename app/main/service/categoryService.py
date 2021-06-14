import uuid
from app.main import db
from app.main.model.category import Category


def new_book(data):
    category = Category.query.filter_by(categoryId=data['categoryId']).first()
    if not category:
        newCategory = category(
            categoryId=uuid.uuid4(),
            categoryName=data['categoryName']
        )
        save_changes(newCategory)
        response_object = {
            'status': 'success',
            'message': 'Successfully Created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Category Already In the System',
        }
        return response_object, 409


def get_all_categories():
    return Category.query.all()


def get_category(cat_name):
    return Category.query.filter_by(cat_name=cat_name).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
