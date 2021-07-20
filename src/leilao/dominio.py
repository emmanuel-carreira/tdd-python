import sys


class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.menor_lance = sys.float_info.max
        self.maior_lance = sys.float_info.min

    def propoe(self, lance: Lance):
        if self.__lances and self.__lances[-1].usuario == lance.usuario:
            raise ValueError(
                "O mesmo usuário não pode dar dois lances seguidos"
            )

        if self.__lances and self.__lances[-1].valor >= lance.valor:
            raise ValueError("O valor do lance deve ser maior do que o último")

        self.__lances.append(lance)
        if lance.valor > self.maior_lance:
            self.maior_lance = lance.valor
        if lance.valor < self.menor_lance:
            self.menor_lance = lance.valor

    @property
    def lances(self):
        return self.__lances[:]
