import unittest
from gestor_contactos import GestorContactos
from contacto import Contacto

class TestSistemaContactos(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorContactos()
        self.contacto = Contacto("Juan", "123456", "juan@mail.com", "Santiago")
        self.gestor.agregar_contacto(self.contacto)

    def test_agregar_contacto(self):
        self.assertEqual(len(self.gestor.contactos), 1)

    def test_buscar_contacto(self):
        resultados = self.gestor.buscar_contacto("Juan")
        self.assertEqual(len(resultados), 1)

    def test_eliminar_contacto(self):
        self.gestor.eliminar_contacto("Juan")
        self.assertEqual(len(self.gestor.contactos), 0)

if __name__ == "__main__":
    unittest.main()
