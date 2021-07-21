import sys

from .excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, valor_carteira):
        self.__nome = nome
        self.__carteira = valor_carteira

    def propoe_lance(self, leilao, valor):
        if self._lance_valido(valor=valor):            
            lance = Lance(usuario=self, valor=valor)
            leilao.propoe(lance=lance)
            self.__carteira -= valor

    def _possui_valor_na_carteira(self, valor):
        if valor <= self.__carteira:
            return True
        raise LanceInvalido("Valor do lance indisponível na carteira")

    def _lance_positivo(self, valor):
        if valor > 0:
            return True
        raise LanceInvalido("Valor do lance deve ser positivo")

    def _lance_valido(self, valor):
        return self._lance_positivo(valor=valor) and self._possui_valor_na_carteira(valor=valor)

    @property
    def carteira(self):
        return self.__carteira

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
        self.menor_lance = None
        self.maior_lance = None

    def propoe(self, lance: Lance):
        if self._lance_valido(lance):
            if not self._tem_lance():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)

    @property
    def lances(self):
        return self.__lances[:]

    def _tem_lance(self):
        return len(self.__lances) != 0

    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido("O mesmo usuário não pode dar dois lances seguidos")

    def _lance_maior_que_anterior(self, lance):
        if self.__lances[-1].valor <= lance.valor:
            return True
        raise LanceInvalido("O valor do lance deve ser maior do que o último")

    def _lance_valido(self, lance):
        return not self._tem_lance() or (self._usuarios_diferentes(lance) and self._lance_maior_que_anterior(lance))
