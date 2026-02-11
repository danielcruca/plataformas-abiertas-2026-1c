from flask import Blueprint, request, jsonify
from app.models.libro import LibroModel
from app.utils.token import token_requerido

libros_endpoints = Blueprint('libros_endpoints', __name__)
 
# GET todos los libros sin parametros y con id.
# Ejemplo de endpoint:
# http://127.0.0.1:5000/libreria/api/v1/libros?id=6823e02cea9cb5e5156c4bd3
# http://127.0.0.1:5000/libreria/api/v1/libros

@libros_endpoints.route('/libros', methods=['GET'])
@token_requerido
def obtenerLibros():
    idLibro = request.args.get('id')

    if idLibro:
        libro = LibroModel.obtener_por_id(idLibro)
        if libro:
            return jsonify(libro), 200
        return jsonify({"error": "Libro no encontrado"}), 404

    libros = LibroModel.obtener_todos()
    return jsonify(libros), 200


@libros_endpoints.route('/hola', methods=['GET'])
@token_requerido
def obtenerHolaMundo():
    return "hola mundo"


@libros_endpoints.route('/libros', methods=['POST'])
@libros_endpoints.route('/libros', methods=['POST'])
def addLibro():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Datos vacíos"}), 400

    # Validar campos principales
    if "titulo" not in data or "autor" not in data or "precio" not in data or "cantidad_stock" not in data:
        return jsonify({"error": "Faltan campos obligatorios del libro"}), 400

    # Validar campos del autor
    autor = data["autor"]
    if "nombre" not in autor or "apellido" not in autor or "nacionalidad" not in autor:
        return jsonify({"error": "Faltan campos obligatorios del autor"}), 400

    # Crear libro
    idLibro = LibroModel.crear(data)
    return jsonify({"id": str(idLibro)}), 200


@libros_endpoints.route('/libros/<idLibro>', methods=['PUT'])
@token_requerido
def updateLibro(idLibro):
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Datos vacios"}), 400
    
    resultado = LibroModel.actualizar(idLibro, data)
    if resultado == -1:
        return jsonify({"error": "Libro no actualizado."}), 404
    

    return jsonify({"Libro actualizado correctamente: ": idLibro}), 200




@libros_endpoints.route('/libros/<id>', methods=['DELETE'])
@token_requerido
def eliminarLibro(id): 
    resultado = LibroModel.eliminar(id)
    if resultado == -1:
        return jsonify({"error": "Libro no eliminado."}), 404

    return jsonify({"mensaje": f"Libro con el id {id} ha sido eliminado correctamente."}), 200
