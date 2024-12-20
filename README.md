# 📚 Backend para Gestión de Lectura de Libros  

Aplicación del lado del servidor que permite **crear**, **ver**, **editar** y **eliminar** libros en una lista de lectura.  

## Características  

- **Crear libros:** Crear nuevos libros en la lista de lectura.  
- **Consultar libros:** Visualizar la lista completa de libros y sus detalles como la descripción, estado ("pendiente", "leído", "en progreso", "abandonado") y puntuación.
- **Actualizar libros:** Editar la información de un libro existente.  
- **Eliminar libros:** Remover libros de la lista de lectura.  


## 📦 Instalación y Ejecución  

### Pasos 
```bash
1. Clonar repositorio
git clone https://github.com/CastanoJenifer/FastApi_Backend.git

2. Instalar las dependencias
pip install -r requirements.txt  

3. Iniciar el servidor
uvicorn src.main:app --reload
```

## 📝 Endpoints
- **GET:** /mostrarLibros: Obtiene los libros de la lista de lectura.
- **POST:** /libros: Crea un nuevo libro en la lista de lectura.
- **PUT:** /editarLibros: Actualiza la información de un libro.
- **DELETE:** /delete_libro:  Elimina un libro.
