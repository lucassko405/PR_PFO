# Sistema de Gestión de Tareas Distribuido

Este proyecto implementa una API REST con Flask para la gestión de tareas, incluyendo registro de usuarios, autenticación y CRUD de tareas. Utiliza SQLite para persistencia de datos y hashing de contraseñas para seguridad.

## Características

- **API REST**: Endpoints para registro, login y gestión de tareas.
- **Autenticación**: Hashing de contraseñas con Werkzeug.
- **Persistencia**: Base de datos SQLite con SQLAlchemy.
- **Cliente en Consola**: Interfaz de línea de comandos para interactuar con la API.

## Requisitos

- Python 3.8+
- Librerías: Flask, Flask-SQLAlchemy, requests

## Instalación

1. Clona el repositorio:
   ```
   git clone <url-del-repositorio>
   cd <nombre-del-repo>
   ```

2. Crea un entorno virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Ejecución

### Servidor
Ejecuta el servidor:
```
python run.py
```
El servidor estará disponible en `http://localhost:5000`.

### Cliente
Ejecuta el cliente:
```
python client/client.py
```

## Endpoints de la API

- `GET /tareas`: Página de bienvenida (HTML).
- `POST /registro`: Registrar un nuevo usuario.
  - Body: `{"username": "usuario", "password": "contraseña"}`
- `POST /login`: Iniciar sesión.
  - Body: `{"username": "usuario", "password": "contraseña"}`
- `GET /tareas/<user_id>`: Listar tareas de un usuario.
- `POST /tareas`: Crear una nueva tarea.
  - Body: `{"titulo": "Título", "descripcion": "Descripción", "usuario_id": 1}`

## Pruebas

### Registro de Usuario
```bash
curl -X POST http://localhost:5000/registro -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpass"}'
```

### Inicio de Sesión
```bash
curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpass"}'
```

### Crear Tarea
```bash
curl -X POST http://localhost:5000/tareas -H "Content-Type: application/json" -d '{"titulo": "Mi tarea", "descripcion": "Descripción", "usuario_id": 1}'
```

### Listar Tareas
```bash
curl http://localhost:5000/tareas/1
```

## Capturas de Pantalla

*(Aquí irían capturas de pantalla de las pruebas exitosas)*

1. Ejecución del servidor.
2. Registro de usuario vía curl.
3. Inicio de sesión.
4. Creación de tarea.
5. Listado de tareas.
6. Interacción con el cliente en consola.

## Respuestas Conceptuales

### ¿Por qué hashear contraseñas?

Hashear contraseñas es crucial para la seguridad porque:
- **Protección contra robo de datos**: Si la base de datos es comprometida, los hashes no revelan las contraseñas originales.
- **Irreversibilidad**: Los algoritmos de hashing como PBKDF2 o bcrypt son de una sola vía, lo que significa que no se pueden "desencriptar".
- **Resistencia a ataques**: Hace que los ataques de fuerza bruta o diccionario sean mucho más difíciles y lentos.
- **Cumplimiento de estándares**: Es una práctica estándar en seguridad de aplicaciones web.

### Ventajas de usar SQLite en este proyecto

- **Simplicidad**: No requiere un servidor de base de datos separado; es un archivo único.
- **Portabilidad**: El archivo de base de datos se puede mover fácilmente entre entornos.
- **Bajo overhead**: Ideal para aplicaciones pequeñas o prototipos sin necesidad de configuración compleja.
- **Integración con Python**: SQLAlchemy facilita el uso de SQLite en aplicaciones Flask.
- **Transacciones ACID**: Garantiza integridad de datos sin configuración adicional.

## Estructura del Proyecto

```
.
├── app/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── client/
│   └── client.py
├── instance/
├── run.py
├── requirements.txt
└── README.md
```

## Contribución

1. Fork el proyecto.
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`).
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`).
4. Push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT.