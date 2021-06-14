from flask_restx import Namespace, fields


class studentDto:
    api = Namespace('student', description='student related operations')
    student = api.model('student', {
        'email': fields.String(required=True, description='student email address'),
        'student_name': fields.String(required=True, description='student name'),
        'password': fields.String(required=True, description='student password'),
        'public_id': fields.String(description='student Identifier')
    })


class bookDto:
    api = Namespace('book', description='book related operations')
    book = api.model('book', {
        'isbnCode': fields.String(required=True, description='isbn code for book'),
        'title': fields.String(required=True, description= 'title for book'),
        'language': fields.String(required=True, description= 'language for book'),
        'available_copies': fields.String(required=True, description='book copies available'),
        'publication_year': fields.String(required=True, description='publication year of book'),
    })


class AuthDto:
    # Two classes of Users need to be authenticated
    # One will be authorized to perform certain special functions
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
