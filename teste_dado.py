import unittest
import dice

#TesteDoModulo main

class test_dado(unittest.TestCase):
    def teste_roda_dado_ok(self):
        teste = dice.rollDice()
        print('Caso de Teste - Condicao de retorno 0 ao lancar dado')
        self.assertTrue(1 <= teste <= 6)

unittest.main()