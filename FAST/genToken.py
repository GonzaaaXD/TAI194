import jwt
from jwt import ExpiredSignatureError, InvalidTokenError

def crear_Token(data:dict):
    token:str = jwt.encode(
        payload = data,
        key = "secretkey",
        algorithm = 'HS256'
    )
    return token

