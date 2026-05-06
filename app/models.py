from . import db  # Importamos la instancia de la DB desde el paquete principal
from werkzeug.security import generate_password_hash, check_password_hash # Para seguridad

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False) # Guardamos el hash, no la clave
    
    # Definimos la relación con las tareas. Un usuario puede tener muchas tareas.
    tareas = db.relationship('Tarea', backref='autor', lazy=True)

    def set_password(self, password):
        # Cifrado de la contraseña para seguridad 
        self.password_hash = generate_password_hash(password) 

    def check_password(self, password):
        # Verifica si la contraseña ingresada coincide con el hash almacenado
        return check_password_hash(self.password_hash, password) 

class Tarea(db.Model):
    __tablename__ = 'tareas'
    # Cada tarea tiene un título, una descripción opcional, un estado de completada o no, y está asociada a un usuario específico.
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))
    completada = db.Column(db.Boolean, default=False)
    
    # Llave foránea: Conecta la tarea con el ID de un usuario[cite: 7]
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)