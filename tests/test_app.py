import unittest
from src.app import soma, eh_par, cadastro_usuario


class TestApp(unittest.TestCase):
    
    def test_soma_numeros_positivo(self):
        resultado = soma(2,5)
        self.assertEqual(resultado, 7 )

    def test_eh_par(self):
        result = eh_par(4)
        self.assertTrue(result)


    def test_eh_impar(self):
        result = eh_par(3)
        self.assertFalse(result)

    def cadastrar_user(self):
        result = cadastro_usuario("Pedro", "pedro@gmail")
        self.assertEqual(result, "Corinthians")
        


if __name__ == '__main__':
    unittest.main()