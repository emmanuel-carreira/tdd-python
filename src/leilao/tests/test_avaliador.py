from unittest import TestCase

from src.leilao.dominio import Avaliador, Lance, Leilao, Usuario


class TestAvaliador(TestCase):

    def setUp(self):
        self.usuario_teste = Usuario(nome="Usuário teste")
        self.usuario_teste_2 = Usuario(nome="Usuário teste 2")

        self.lance_150 = Lance(usuario=self.usuario_teste, valor=150.00)
        self.lance_200 = Lance(usuario=self.usuario_teste_2, valor=200.00)

        self.leilao = Leilao(descricao="Leilão teste")

        self.avaliador = Avaliador()

    def test_avalia_lances_crescentes(self):
        self.leilao.lances.append(self.lance_150)
        self.leilao.lances.append(self.lance_200)

        self.avaliador.avalia(leilao=self.leilao)

        maior_lance_esperado = 200.00
        menor_lance_esperado = 150.00

        self.assertEqual(maior_lance_esperado, self.avaliador.maior_lance)
        self.assertEqual(menor_lance_esperado, self.avaliador.menor_lance)


    def test_avalia_lances_decrescentes(self):
        self.leilao.lances.append(self.lance_200)
        self.leilao.lances.append(self.lance_150)

        self.avaliador.avalia(leilao=self.leilao)

        maior_lance_esperado = 200.00
        menor_lance_esperado = 150.00

        self.assertEqual(maior_lance_esperado, self.avaliador.maior_lance)
        self.assertEqual(menor_lance_esperado, self.avaliador.menor_lance)

    def test_avalia_um_lance(self):
        self.leilao.lances.append(self.lance_200)

        self.avaliador.avalia(leilao=self.leilao)

        maior_lance_esperado = 200.00
        menor_lance_esperado = 200.00

        self.assertEqual(maior_lance_esperado, self.avaliador.maior_lance)
        self.assertEqual(menor_lance_esperado, self.avaliador.menor_lance)

    def test_avalia_lances_aleatorios(self):
        self.leilao.lances.append(self.lance_200)
        self.leilao.lances.append(self.lance_150)

        usuario_teste_3 = Usuario("Usuario teste 3")
        lance_300 = Lance(usuario=usuario_teste_3, valor=300.00)
        self.leilao.lances.append(lance_300)

        self.avaliador.avalia(leilao=self.leilao)

        maior_lance_esperado = 300.00
        menor_lance_esperado = 150.00

        self.assertEqual(maior_lance_esperado, self.avaliador.maior_lance)
        self.assertEqual(menor_lance_esperado, self.avaliador.menor_lance)
