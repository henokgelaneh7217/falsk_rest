from app.main import db
from app.main.model.author import Author


def new_author(data):
    author = Author.query.filter_by(authorId=data['authorId']).first()
    if not author:
        newAuthor = author(
            authorId=data['authorId'],
            authorName=data['authorName']
        )
        save_changes(newAuthor)
        response_object = {
            'status': 'success',
            'message': 'Successfully Added.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Author already in the system',
        }
        return response_object, 409


def get_all_authors():
    return Author.query.all()


def get_author(authorName):
    return Author.query.filter_by(authorName=authorName).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
