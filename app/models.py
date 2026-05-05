from . import db  # Importamos la instancia de la DB desde el paquete principal
from werkzeug.security import generate_password_hash, check_password_hash # Para seguridad

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False) # Guardamos el hash, no la clave
    
    # Definimos la relación: permite acceder a las tareas desde el objeto usuario[cite: 6]
    tareas = db.relationship('Tarea', backref='autor', lazy=True)

    def set_password(self, password):
        """Genera un hash seguro a partir de la contraseña."""
        self.password_hash = generate_password_hash(password) # Cifrado profesional[cite: 7]

    def check_password(self, password):
        """Verifica si la contraseña coincide con el hash guardado."""
        return check_password_hash(self.password_hash, password)

class Tarea(db.Model):
    __tablename__ = 'tareas'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))
    completada = db.Column(db.Boolean, default=False)
    
    # Llave foránea: Conecta la tarea con el ID de un usuario[cite: 7]
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)