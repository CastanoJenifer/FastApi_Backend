from fastapi import FastAPI
from app.routes import example_routes

app = FastAPI()

# Registrar las rutas del proyecto
app.include_router(example_routes.router)

@app.get("/")
async def root():
    return {"message": "¡Backend funcionando!"}
