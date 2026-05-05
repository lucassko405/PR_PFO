from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializamos la base de datos fuera de la función para que sea accesible
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuración de persistencia y seguridad
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gestion_tareas.db'
    app.config['SECRET_KEY'] = 'una_clave_secreta_123' # Para proteger la sesión
    
    db.init_app(app)

    with app.app_context():
        # Importamos las rutas aquí para evitar "importaciones circulares"
        from . import routes
        # Crea el archivo .db físicamente si no existe[cite: 7]
        db.create_all() 
        
    return app