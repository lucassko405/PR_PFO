from app import create_app

app = create_app()

if __name__ == '__main__':
    # threaded=True permite manejar múltiples clientes a la vez
    app.run(debug=True, port=5000, threaded=True)