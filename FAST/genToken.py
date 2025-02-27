import jwt

def crear_Token(data:dict):
    token:str = jwt.encode(
        payload = data,
        key = "secretkey",
        algorithm = 'HS256'
    )
    return token