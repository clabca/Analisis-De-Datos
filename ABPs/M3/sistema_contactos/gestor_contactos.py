from contacto import Contacto

class GestorContactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def eliminar_contacto(self, nombre):
        self.contactos = [
            c for c in self.contactos if c.get_nombre().lower() != nombre.lower()
        ]

    def buscar_contacto(self, criterio):
        return [
            c for c in self.contactos
            if criterio.lower() in c.get_nombre().lower()
            or criterio in c.get_telefono()
        ]

    def editar_contacto(self, nombre, telefono=None, correo=None, direccion=None):
        for contacto in self.contactos:
            if contacto.get_nombre().lower() == nombre.lower():
                if telefono:
                    contacto.set_telefono(telefono)
                if correo:
                    contacto.set_correo(correo)
                if direccion:
                    contacto.set_direccion(direccion)
