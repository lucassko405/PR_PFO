from app import create_app
# Este archivo es el punto de entrada de la aplicación Flask.
# Aquí se crea la instancia de la aplicación y se ejecuta el servidor.
app = create_app()

if __name__ == '__main__':
    # threaded=True permite manejar múltiples clientes a la vez
    # definimos el puerto para evitar conflictos con otros servicios
    app.run(debug=True, port=5000, threaded=True)