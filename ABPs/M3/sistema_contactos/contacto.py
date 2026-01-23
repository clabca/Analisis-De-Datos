class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__correo = correo
        self.__direccion = direccion

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_telefono(self):
        return self.__telefono

    def get_correo(self):
        return self.__correo

    def get_direccion(self):
        return self.__direccion

    # Setters
    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_correo(self, correo):
        self.__correo = correo

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def to_dict(self):
        return {
            "nombre": self.__nombre,
            "telefono": self.__telefono,
            "correo": self.__correo,
            "direccion": self.__direccion
        }
