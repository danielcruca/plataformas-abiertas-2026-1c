from functools import wraps
from flask import request, jsonify
from datetime import datetime
from app import mongo


def token_requerido(funcion_original):
    @wraps(funcion_original)
    def verificaToken(*args, **kwargs):

        # 1 obtiene el token del header.
        # 2 valida que el token no sea nulo.
        # 3 que el token si exista en mongo.
        # 4 verifica que la fecha de expiracion sea mayor a la actual.
        
        auth = request.headers.get("Authorization")
        if not auth or  not auth .startswith("Bearer "):
            return jsonify({"error": "token  requerido."}), 401
        # Bearer 123
        token = auth.split(" ")[1] 
        colecion_tokens = mongo.db.tokens # obtener la colecion de tokens desde mongo.

        documento_token = colecion_tokens.find_one({"token": token})


        if not documento_token:
            return jsonify({"error": "token no valido."}), 401

        if datetime.now() > documento_token["expiracion"]:
            return jsonify({"error": "token expirado."}), 401

        return funcion_original(*args, **kwargs)

    return verificaToken
        
