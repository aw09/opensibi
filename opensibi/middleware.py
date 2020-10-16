from functools import wraps
from opensibi.jwt import JWTAuth
from rest_framework.response import Response


def jwtRequired(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            decode(args[0].headers.get('Authorization'))
        except Exception as e:
            return Response(data="unauthorized()")
        return fn(*args, **kwargs)

    return wrapper


def decode(token):
    token = str(token).split(' ')
    return JWTAuth().decode(token[1])