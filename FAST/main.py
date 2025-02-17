from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title = "Mi primer API",
    description = "Gonzalo Uribe Arteaga",
    version = "1.0.1"
)

usuarios = [
    {"id":1, "nombre":"Gonzalo", "edad":21},
    {"id":2, "nombre":"Estrella", "edad":21},
    {"id":3, "nombre":"Pepe", "edad":21},
    {"id":4, "nombre":"Perla", "edad":21},
]

#ruta o EndPoint
@app.get('/', tags = ['Inicio'])
def home():
    return {'hello': 'world fastApi'}

@app.get('/todosUsuarios', tags = ['Operaciones CRUD'])
def leer():
    return {'Usuarios Registrados' : usuarios}

#endpoint post
@app.post('/usuarios/', tags = ['Operaciones CRUD'])
def insert(usuario:dict):
    for usr in usuarios:
        if usr["id"]==usuario.get("id"):
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    usuarios.append(usuario)
    return usuario

#endpoint put
@app.put('/usuarios/{id}', tags = ['Operaciones CRUD'])
def update(id:int, usuarioActulizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActulizado)
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")

@app.delete('/usuarios/eliminar', tags = ['Operaciones CRUD'])
def borrar(id:int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            del usuarios[index]
            return f"Se removio el usuario con el id: {id}"
        raise HTTPException(status_code=400, detail="El usuario no existe")
            