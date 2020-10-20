
import unittest
from unittest import mock
import dice

class testa_num_jogadores(unittest.TestCase):
    def define_teste(self):
        m = mock.Mock()
        assert isinstance(m.campo,mock.Mock)
        assert isinstance(m(),mock.Mock)

    def teste_atribui(self):
        m = mock.Mock()
        m.num = 2
        self.assertEqual(m.num,2)

    def teste_jogador(self):
        m = mock.Mock()
        m.retornaJogador.return_value = 2
        self.assertEqual(m.retornaJogador(),2)


class test_dado(unittest.TestCase):
    def teste_roda_dado_ok(self):
        teste = dice.rollDice()
        print('Caso de Teste - Condicao de retorno 0 ao lancar dado')
        self.assertTrue(1 <= teste <= 6)

unittest.main()