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
            return libros
        except DoesNotExist:
            return None

    @staticmethod
    async def update_libro(libro_id: int, libro_data):
        try:
            libro_obj = await Gestor.get(id=libro_id)
            libro_obj.titulo = libro_data.titulo
            libro_obj.descripcion = libro_data.descripcion
            libro_obj.estado = libro_data.estado
            libro_obj.puntuacion = libro_data.puntuacion
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
