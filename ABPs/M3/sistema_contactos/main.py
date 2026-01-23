from gestor_contactos import GestorContactos
from contacto import Contacto
import json
import os

# Ruta absoluta del archivo contactos.json en la misma carpeta de main.py
CARPETA_BASE = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_CONTACTOS = os.path.join(CARPETA_BASE, "contactos.json")

# Funciones para guardar y cargar contactos
def guardar_contactos(contactos, archivo=ARCHIVO_CONTACTOS):
    with open(archivo, "w") as f:
        json.dump([c.to_dict() for c in contactos], f, indent=4)  # indent para leer fácil

def cargar_contactos(archivo=ARCHIVO_CONTACTOS):
    contactos = []
    try:
        with open(archivo, "r") as f:
            datos = json.load(f)
            for d in datos:
                contactos.append(Contacto(d["nombre"], d["telefono"], d["correo"], d["direccion"]))
    except FileNotFoundError:
        pass  # si no existe el archivo, empieza vacío
    return contactos

# Inicializamos gestor y cargamos contactos existentes
gestor = GestorContactos()
gestor.contactos = cargar_contactos()

# Menú de la aplicación
def menu():
    print("\n--- Sistema de Gestión de Contactos ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Editar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        direccion = input("Dirección: ")
        gestor.agregar_contacto(Contacto(nombre, telefono, correo, direccion))
        guardar_contactos(gestor.contactos)
        print("Contacto agregado correctamente.")

    elif opcion == "2":
        criterio = input("Buscar por nombre o teléfono: ")
        resultados = gestor.buscar_contacto(criterio)
        if resultados:
            for c in resultados:
                print(c.to_dict())
        else:
            print("No se encontraron contactos.")

    elif opcion == "3":
        nombre = input("Nombre del contacto a editar: ")
        telefono = input("Nuevo teléfono (Enter para omitir): ")
        correo = input("Nuevo correo (Enter para omitir): ")
        direccion = input("Nueva dirección (Enter para omitir): ")
        gestor.editar_contacto(
            nombre,
            telefono if telefono else None,
            correo if correo else None,
            direccion if direccion else None
        )
        guardar_contactos(gestor.contactos)
        print("Contacto actualizado.")

    elif opcion == "4":
        nombre = input("Nombre del contacto a eliminar: ")
        gestor.eliminar_contacto(nombre)
        guardar_contactos(gestor.contactos)
        print("Contacto eliminado.")

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")
