from tortoise import fields, models

class Gestor(models.Model):
    id = fields.IntField(pk=True, auto_increment=True)
    titulo = fields.CharField(max_length=255)
    descripcion = fields.TextField(null=True)
    estado = fields.CharField(max_length=20, choices=["pendiente", "leído", "en progreso", "abandonado"])
    puntuacion = fields.IntField(null=True)
    fecha_creacion = fields.DatetimeField(null=False, auto_now_add=True)

    class Meta:
        table = "libros"