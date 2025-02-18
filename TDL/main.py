from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title = "To-Do-List",
    description = "Gonzalo Uribe Arteaga",
    version = "1.0.1"
)

tareas = [
    {
        "id": 1,
        "titulo": "Estudiar para el examen",
        "descripcion": "Repasar los apuntes de TAI ",
        "vencimiento": "14-02-25",
        "Estado": "completada"
    },
    {
        "id": 2,
        "titulo": "Terminar sistema",
        "descripcion": "Completar el programa de sistemas inteligentes",
        "vencimiento": "17-02-25",
        "Estado": "no completada"
    },
    {
        "id": 3,
        "titulo": "Crear vpn",
        "descripcion": "Hacer una vpn para virtualización",
        "vencimiento": "18-02-25",
        "Estado": "no completada"
    },
]

@app.get('/tareas', tags = ['Lista de tareas'])
def leer():
    return {'Tareas Registrados' : tareas}

@app.get('/tareas/{id}', tags=['Buscar tarea'])
def consultarTarea(id: Optional[int] = None):
    if id is not None:
        for tarea in tareas:
            if tarea["id"] == id:
                return {"mensaje": "Tarea encontrada", "Tarea": tarea}
        return {"mensaje": f"No se encontró el id: {id}"}
    return {"mensaje": "No se proporcionó un id"}

#endpoint post
@app.post('/nuevaTarea/', tags = ['Agregar tarea'])
def insert(tarea:dict):
    for tar in tareas:
        if tar["id"]== tarea.get("id"):
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    tareas.append(tarea)
    return tarea

#endpoint put
@app.put('/tareas/{id}/actualizar', tags = ['Actualizar'])
def update(id:int, tareaActulizada:dict):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == id:
            tareas[index].update(tareaActulizada)
            return tareas[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")

@app.delete('/tareas/eliminar={id}', tags=['Eliminar tarea'])
def borrar(id: int):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == id:
            del tareas[index]
            return {"mensaje": f"Se eliminó la tarea con el id: {id}"}
    
    raise HTTPException(status_code=404, detail=f"No se encontró una tarea con el id: {id}")