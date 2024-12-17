from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.routes import gestor_routes

app = FastAPI()

# Registrar las rutas del proyecto
app.include_router(gestor_routes.router)

@app.get("/")
async def root():
    return {"message": "¡Backend funcionando!"}


# Conexión con la base de datos
register_tortoise(
    app,
    db_url="postgres://postgres:12345@localhost:5432/gestorbiblioteca",
    modules={"models": ["app.models.gestor_model"]},
    generate_schemas=True,
    add_exception_handlers=True,
)