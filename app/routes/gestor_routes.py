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

class EditarIn(BaseModel):
    id: int
    titulo: str
    descripcion: str | None
    estado:str  
    puntuacion: int | None 

class EditarOut(EditarIn):
    titulo: str
    descripcion: str | None
    estado:str  
    puntuacion: int | None 
    
    class config:
        orm_mode = True 
        
class EliminarIn(BaseModel):
    id: int

@router.post("/libros", response_model=LibrosOut)
async def create_libro(libros: LibrosIn):
    libro_obj = await GestorController.create_libro(libros.titulo,libros.descripcion, libros.estado, libros.puntuacion)
    return libro_obj
        
@router.get("/mostrarLibros")
async def conseguir_libros():
    libros = await GestorController.read_libros()
    return libros

@router.put("/editarLibros", response_model=LibrosOut)
async def editar_libros(libros: EditarIn):
    libro_obj = await GestorController.update_libro(libros.id, libros.titulo,libros.descripcion, libros.estado, libros.puntuacion)
    return libro_obj

@router.delete("/delete_libro")
async def eliminar_libros(libros: EliminarIn):
    eliminado = await GestorController.delete_libro(libros.id)
    return eliminado