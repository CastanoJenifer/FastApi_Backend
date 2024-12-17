from fastapi import APIRouter, HTTPException
from app.controllers.gestor_controllers import GestorController
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class LibrosIn(BaseModel):
    titulo: str
    descripcion: str | None
    estado:str  
    puntuacion: int | None 

class LibrosOut(LibrosIn):
    id: int
    fecha_creacion: datetime
    
    class config:
        orm_mode = True
    

@router.post("/libros", response_model=LibrosOut)
async def create_tarea(libros: LibrosIn):
    libro_obj = await GestorController.create_libro(libros.titulo,libros.descripcion, libros.estado, libros.puntuacion)
    return libro_obj
    