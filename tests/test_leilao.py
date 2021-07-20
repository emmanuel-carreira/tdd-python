from unittest import TestCase

from src.leilao.dominio import Lance, Leilao, Usuario


class TestLeilao(TestCase):

    def setUp(self):
        self.usuario_teste = Usuario(
            nome="Usuário teste", valor_carteira=1000.00
        )
        self.usuario_teste_2 = Usuario(
            nome="Usuário teste 2", valor_carteira=1500.00
        )

        self.lance_150 = Lance(usuario=self.usuario_teste, valor=150.00)
        self.lance_200 = Lance(usuario=self.usuario_teste_2, valor=200.00)

        self.leilao = Leilao(descricao="Leilão teste")

    def test_avalia_lances_crescentes(self):
        self.leilao.propoe(lance=self.lance_150)
        self.leilao.propoe(lance=self.lance_200)

        maior_lance_esperado = 200.00
        menor_lance_esperado = 150.00

        self.assertEqual(maior_lance_esperado, self.leilao.maior_lance)
        self.assertEqual(menor_lance_esperado, self.leilao.menor_lance)


    def test_invalida_lances_decrescentes(self):
        with self.assertRaises(ValueError):
            self.leilao.propoe(lance=self.lance_200)
            self.leilao.propoe(lance=self.lance_150)

    def test_avalia_um_lance(self):
        self.leilao.propoe(lance=self.lance_200)

        maior_lance_esperado = 200.00
        menor_lance_esperado = 200.00

        self.assertEqual(maior_lance_esperado, self.leilao.maior_lance)
        self.assertEqual(menor_lance_esperado, self.leilao.menor_lance)

    def test_permite_lance_inicial(self):
        self.leilao.propoe(lance=self.lance_200)

        self.assertEqual(1, len(self.leilao.lances))

    def test_permite_lance_usuario_diferente(self):
        self.leilao.propoe(lance=self.lance_150)
        self.leilao.propoe(lance=self.lance_200)

        self.assertEqual(2, len(self.leilao.lances))

    def test_nao_permite_lance_mesmo_usuario(self):
        with self.assertRaises(ValueError):
            self.leilao.propoe(lance=self.lance_150)
            lance_175 = Lance(usuario=self.usuario_teste, valor=175.00)
            self.leilao.propoe(lance=lance_175)
