# La función calcula el doble de un número.
def duplicar(numero):
    return numero * 2
 
# La prueba comprueba un resultado específico.
import unittest
 
class PruebaDuplicar(unittest.TestCase):
    def test_doble_de_tres(self):
        self.assertEqual(duplicar(3), 6)
 
# Una salida breve y estable para este ejemplo.
resultado = unittest.TestResult()
PruebaDuplicar("test_doble_de_tres").run(resultado)
print("Pruebas ejecutadas:", resultado.testsRun)
print("Resultado correcto:", resultado.wasSuccessful())
