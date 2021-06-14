import datetime
import jwt
from ..config import key
from typing import Union


def token_encode(studentId: int) -> bytes:
    try:
        to_be_encoded = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': studentId
        }
        return jwt.encode(
            to_be_encoded, key, algorithm='HS256'
        )
    except Exception as e:
        return e


def token_decode(token: str) -> Union[str, int]:
    try:
        decoded = jwt.decode(token, key)
        return decoded['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
