from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List
from models import modelUsuario  # Asegúrate de que esté bien definido en models.py

app = FastAPI(
    title="Mi primer API",
    description="Gonzalo Uribe Arteaga",
    version="1.0.1"
)

usuarios = [
    {"id": 1, "nombre": "Gonzalo", "edad": 21, "correo": "gonzalo@gmail.com"},
    {"id": 2, "nombre": "Estrella", "edad": 21, "correo": "estrella@gmail.com"},
    {"id": 3, "nombre": "Pepe", "edad": 21, "correo": "pepe@gmail.com"},
    {"id": 4, "nombre": "Perla", "edad": 21, "correo": "perla@gmail.com"},
]

# Ruta de inicio
@app.get("/", tags=["Inicio"])
def home():
    return {"hello": "world fastApi"}

# Obtener todos los usuarios
@app.get("/todosUsuarios", response_model=List[modelUsuario], tags=["Operaciones CRUD"])
def leer():
    return usuarios

# Insertar usuario
@app.post("/usuarios/", response_model=modelUsuario, tags=["Operaciones CRUD"])
def insert(usuario: modelUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    usuarios.append(usuario.model_dump())  # Convertimos a diccionario
    return usuario

# Actualizar usuario
@app.put("/usuarios/{id}", response_model=modelUsuario, tags=["Operaciones CRUD"])
def update(id: int, usuario_actualizado: modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuario_actualizado.model_dump()  # Convertimos a diccionario
            return usuarios[index]
    
    raise HTTPException(status_code=404, detail="El usuario no existe")

# Eliminar usuario
@app.delete("/usuarios/eliminar", tags=["Operaciones CRUD"])
def borrar(id: int = Query(..., description="ID del usuario a eliminar")):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            del usuarios[index]
            return {"mensaje": f"Se removió el usuario con el id: {id}"}
    
    raise HTTPException(status_code=404, detail="El usuario no existe")
