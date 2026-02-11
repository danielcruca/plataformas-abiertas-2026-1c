 # 1. Crea un archivo .env en la raíz del proyecto

Agregar en una variable la conexion a mongodb.

Por ejemplo:

```python
    MONGO_URI=mongodb+srv://docentedanielcr:SU-PASSWORD@cluster0.rnphuit.mongodb.net/libreria?retryWrites=true&w=majority
```

 # 2.Instalar python-dotenv 

```bash
pip install python-dotenv   
```
# ✅ 3. Modifica tu create_app() para cargar variables del .env

El codigo se debe de modicar algo asi, notar los comentarios que dicen #acá
```python
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv #acá
import os #acá

mongo = PyMongo()

def create_app():
    # Cargar variables del .env
    load_dotenv() #acá

    app = Flask(__name__)

    # Leer la URI desde el entorno
    uri = os.getenv("MONGO_URI")

    app.config["MONGO_URI"] = uri #acá
    mongo.init_app(app)

    app.config["MONGO_CLIENT"] = MongoClient(uri)

    CORS(app, origins="*")

    from .controllers.libros import libros_endpoints
    app.register_blueprint(libros_endpoints, url_prefix="/libreria/api/v1")

    return app

```    
Si tiene dudas, puede ver la implementación en *libreria-con-get-insert-ejemplo*.

# Git Agregar el archivo .env a gitignore

Editar el archivo .gitignore y agregar la siguiente linea:

`.env`

Esto es para no subir el string de conexion de la base de datos a github.
