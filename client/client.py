import requests

BASE_URL = "http://localhost:5000"

session_user_id = None  # Aquí guardaremos el ID del usuario logueado

def menu():
    print("\n--- SISTEMA DE TAREAS DISTRIBUIDO ---")
    print("1. Registrarse")
    print("2. Iniciar Sesión y ver tareas")
    print("3. Salir")
    return input("Selecciona una opción: ")

def ejecutar_registro():
    user = input("Usuario: ")
    pw = input("Contraseña: ")
    resp = requests.post(f"{BASE_URL}/registro", json={"username": user, "password": pw})
    print(resp.json().get("mensaje") or resp.json().get("error"))

# ... aquí iría la lógica de login y tareas ...



def ejecutar_login():
    global session_user_id
    user = input("Usuario: ")
    pw = input("Contraseña: ")
    resp = requests.post(f"{BASE_URL}/login", json={"username": user, "password": pw})
    
    if resp.status_code == 200:
        session_user_id = resp.json().get("usuario_id")
        print(f"✅ {resp.json().get('mensaje')}")
        gestion_tareas()
    else:
        print(f"❌ {resp.json().get('error')}")

def gestion_tareas():
    while True:
        print("\n--- MIS TAREAS ---")
        print("1. Ver mis tareas")
        print("2. Crear nueva tarea")
        print("3. Cerrar sesión")
        op = input("Selecciona: ")
        
        if op == "1":
            resp = requests.get(f"{BASE_URL}/tareas/{session_user_id}")
            for t in resp.json():
                estado = "✔" if t['completada'] else "❌"
                print(f"[{estado}] {t['id']}: {t['titulo']}")
        
        elif op == "2":
            titulo = input("Título de la tarea: ")
            desc = input("Descripción: ")
            requests.post(f"{BASE_URL}/tareas", json={
                "titulo": titulo, "descripcion": desc, "usuario_id": session_user_id
            })
            print("🚀 Tarea enviada al servidor.")
            
        elif op == "3":
            break

if __name__ == "__main__":
    while True:
        opcion = menu()
        if opcion == "1": ejecutar_registro()
        if opcion == "2": ejecutar_login()
        elif opcion == "3": break

# ... (mantén el bloque if __name__ == "__main__" del paso anterior llamando a ejecutar_login)