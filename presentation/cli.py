def run_cli(service):
    user_id = int(input("Ingrese ID del usuario: "))

    try:
        user = service.upgrade_user(user_id)
        print(f"Usuario {user.name} ahora es Premium.")
    except Exception as e:
        print("Error:", str(e))