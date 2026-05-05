from flask import request, jsonify
from flask import current_app as app
from .models import db, Usuario, Tarea

@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json() # Recibimos datos del cliente vía red
    if Usuario.query.filter_by(username=data['username']).first():
        return jsonify({"error": "El usuario ya existe"}), 400
    
    nuevo_usuario = Usuario(username=data['username'])
    nuevo_usuario.set_password(data['password']) # Hasheo automático[cite: 7]
    
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario creado con éxito"}), 201

@app.route('/login', methods=['POST'])


def login():
    data = request.get_json()
    usuario = Usuario.query.filter_by(username=data['username']).first()
    
    if usuario and usuario.check_password(data['password']):
        return jsonify({"mensaje": "Login exitoso", "usuario_id": usuario.id}), 200
    
    return jsonify({"error": "Credenciales inválidas"}), 401

@app.route('/tareas/<int:user_id>', methods=['GET'])


def listar_tareas(user_id):
    usuario = Usuario.query.get(user_id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
        
    # List comprehension para convertir objetos a JSON[cite: 7]
    tareas = [{"id": t.id, "titulo": t.titulo, "completada": t.completada} for t in usuario.tareas]
    return jsonify(tareas), 200

# Agrega esto al final de app/routes.py

@app.route('/tareas', methods=['POST'])
def crear_tarea():
    data = request.get_json()
    # Verificamos que el usuario exista antes de crear la tarea
    usuario = Usuario.query.get(data['usuario_id'])
    if not usuario:
        return jsonify({"error": "Usuario no autorizado"}), 401
    
    nueva_tarea = Tarea(
        titulo=data['titulo'],
        descripcion=data.get('descripcion', ''),
        usuario_id=usuario.id
    )
    
    db.session.add(nueva_tarea)
    db.session.commit()
    return jsonify({"mensaje": "Tarea creada con éxito", "id": nueva_tarea.id}), 201