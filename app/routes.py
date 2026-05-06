from flask import request, jsonify # Importamos request para manejar las solicitudes entrantes y jsonify para formatear las respuestas en JSON. 
from flask import current_app as app
from .models import db, Usuario, Tarea

# Ruta básica para verificar que la API está funcionando correctamente.
# Evita el error 404 al acceder a la raíz desde el navegador.

@app.route('/')
def home():
    return "<h2>API de tareas funcionando </h2>"


# Permite crear un nuevo usuario. Recibe JSON con username y password.

@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()

    # Validación de datos obligatorios
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Faltan datos"}), 400

    # Verifica si el usuario ya existe
    if Usuario.query.filter_by(username=data['username']).first():
        return jsonify({"error": "El usuario ya existe"}), 400
    
    # Creación del usuario con contraseña hasheada
    nuevo_usuario = Usuario(username=data['username'])
    nuevo_usuario.set_password(data['password'])
    
    db.session.add(nuevo_usuario)
    # Guardamos los cambios en la base de datos
    db.session.commit()
    return jsonify({"mensaje": "Usuario creado con éxito"}), 201


# Permite autenticar un usuario existente.
# Devuelve el id del usuario si las credenciales son correctas.

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validación de datos
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Faltan datos"}), 400

    usuario = Usuario.query.filter_by(username=data['username']).first()
    
    # Verificación de credenciales
    if usuario and usuario.check_password(data['password']):
        return jsonify({
            "mensaje": "Login exitoso",
            "usuario_id": usuario.id
        }), 200
    
    return jsonify({"error": "Credenciales inválidas"}), 401



# Ruta solicitada por el cliente para mostrar las tareas de un usuario específico.
@app.route('/tareas', methods=['GET'])
def tareas_home():
    # Devuelve una respuesta en HTML para visualizar en navegador.
    return "<h1>Bienvenido al sistema de tareas</h1>"


# Devuelve todas las tareas asociadas a un usuario específico.
# Se accede mediante el id del usuario en la URL.

@app.route('/tareas/<int:user_id>', methods=['GET'])
def listar_tareas(user_id):
    usuario = Usuario.query.get(user_id)

    # Validación de existencia del usuario
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
        
    # Conversión de objetos a formato JSON
    tareas = [
        {
            "id": t.id,
            "titulo": t.titulo,
            "descripcion": t.descripcion,
            "completada": t.completada
        }
        for t in usuario.tareas
    ]

    return jsonify(tareas), 200


# Permite crear una nueva tarea asociada a un usuario.

@app.route('/tareas', methods=['POST'])
def crear_tarea():
    data = request.get_json()

    # Validación de datos obligatorios
    if not data or not data.get('titulo') or not data.get('usuario_id'):
        return jsonify({"error": "Faltan datos"}), 400

    # Verifica que el usuario exista
    usuario = Usuario.query.get(data['usuario_id'])

    if not usuario:
        return jsonify({"error": "Usuario no autorizado"}), 401
    
    # Creación de la tarea
    nueva_tarea = Tarea(
        titulo=data['titulo'],
        descripcion=data.get('descripcion', ''),
        usuario_id=usuario.id
    )
    
    db.session.add(nueva_tarea)
    db.session.commit()

    return jsonify({
        "mensaje": "Tarea creada con éxito",
        "id": nueva_tarea.id
    }), 201