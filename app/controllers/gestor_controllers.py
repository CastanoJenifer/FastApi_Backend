from app.models.gestor_model import Gestor
from tortoise.exceptions import DoesNotExist
from datetime import datetime

class GestorController:
    @staticmethod
    async def create_libro(titulo, descripcion, estado, puntuacion):
        libro_obj = await Gestor.create(titulo= titulo, descripcion=descripcion, estado=estado, puntuacion=puntuacion)
        return libro_obj

    @staticmethod
    async def read_libros():
        try:
            libros = await Gestor.all()
            if libros is None:
                return "No hay libros aún"
            else:
                return libros
        except DoesNotExist:
            return None

    @staticmethod
    async def update_libro(id_libro, titulo, descripcion, estado, puntuacion):
        try:
            libro_obj = await Gestor.get(id=id_libro)
            libro_obj.titulo = titulo
            libro_obj.descripcion = descripcion
            libro_obj.estado = estado
            libro_obj.puntuacion = puntuacion
            await libro_obj.save()
            return libro_obj
        except DoesNotExist:
            return None

    @staticmethod
    async def delete_libro(libro_id: int):
        try:
            libro = await Gestor.get(id=libro_id)
            await libro.delete()
            return True
        except DoesNotExist:
            return False
