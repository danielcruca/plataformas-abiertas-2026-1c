from bson.objectid import ObjectId
from app import mongo

class LibroModel:
    @staticmethod
    def obtener_todos():
        libros_cursor = mongo.db.libros.find()
        libros = []
        for libro in libros_cursor:
            libro["_id"] = str(libro["_id"]) # Esto convierte el ObjectId en una cadena.
            libros.append(libro)
        return libros

    @staticmethod
    def obtener_por_id(id):
        try:
            libro = mongo.db.libros.find_one({"_id": ObjectId(id)})
            if libro:
                libro["_id"] = str(libro["_id"])   # Esto convierte el ObjectId en una cadena.
            return libro
        except:
            return None

    @staticmethod
    def crear(libro):
        print("en el modelo")
        print(libro)
        try:
            result = mongo.db.libros.insert_one(libro)
            return result.inserted_id
        except Exception as e:
            return None
        
    @staticmethod
    def actualizar(id, data):
        try:
            result = mongo.db.libros.update_one({"_id": ObjectId(id)}, {"$set": data})
            return result.modified_count
        except:
            return -1
        
    @staticmethod
    def eliminar(id):
        try:
            result = mongo.db.libros.delete_one({"_id": ObjectId(id)})
            return result.deleted_count
        except:
            return -1
        
