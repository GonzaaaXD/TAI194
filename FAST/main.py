from fastapi import FastAPI

app = FastAPI()

#ruta o EndPoint
@app.get('/')
def home():
    return {'hello': 'world fastApi'}

#Endpoint promedio
@app.get('/promedio')
def promedio():
    return 10.5

@app.get('/usuario/{id}')
def consultarUsuario(id : int):
    return "Se encontro el usuario: {id}"