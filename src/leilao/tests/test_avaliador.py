from unittest import TestCase

from src.leilao.dominio import Avaliador, Lance, Leilao, Usuario


class TestAvaliador(TestCase):

    def test_avalia(self):
        usuario = Usuario(nome="Usuário teste")

        lance = Lance(usuario=usuario, valor=200.00)
        lance_2 = Lance(usuario=usuario, valor=150.00)

        leilao = Leilao(descricao="Leilão teste")
        leilao.lances.append(lance)
        leilao.lances.append(lance_2)

        avaliador = Avaliador()
        avaliador.avalia(leilao=leilao)

        maior_lance_esperado = 200.00
        menor_lance_esperado = 150.00

        self.assertEqual(maior_lance_esperado, avaliador.maior_lance)
        self.assertEqual(menor_lance_esperado, avaliador.menor_lance)
