from tortoise import Tortoise

TORTOISE ={
   "connections": {
       "default" : "postgres://postgres:12345@localhost:5432/gestorbiblioteca"
   },
   "apps": {
       "models": {
           "models": ["app.models.gestor_model"],
           "default_connection": "default",
       }
   }

}

async def init():
    await Tortoise.init(config=TORTOISE)
    await Tortoise.generate_schemas()