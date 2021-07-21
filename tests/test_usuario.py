import pytest

from src.leilao.dominio import Leilao, Usuario
from src.leilao.excecoes import LanceInvalido


@pytest.fixture
def usuario():
    return Usuario(nome="Usuário de teste", valor_carteira=500.00)


@pytest.fixture
def leilao():
    return Leilao(descricao="Venda de celular")


def test_subtrair_valor_carteira_lance_bem_sucedido(usuario, leilao):
    usuario.propoe_lance(leilao=leilao, valor=200.00)
    assert usuario.carteira == 300.00


def test_aceita_lance_valor_menor_que_carteira(usuario, leilao):
    usuario.propoe_lance(leilao=leilao, valor=400.00)
    assert usuario.carteira == 100.00


def test_aceita_lance_valor_igual_a_carteira(usuario, leilao):
    usuario.propoe_lance(leilao=leilao, valor=500.00)
    assert usuario.carteira == 0.00


def test_aceita_lance_valor_maior_que_carteira(usuario, leilao):
    with pytest.raises(LanceInvalido):
        usuario.propoe_lance(leilao=leilao, valor=1000.00)


def test_nao_aceita_lance_negativo(usuario, leilao):
    with pytest.raises(LanceInvalido):
        usuario.propoe_lance(leilao=leilao, valor=-10.00)


def test_nao_aceita_lance_zero(usuario, leilao):
    with pytest.raises(LanceInvalido):
        usuario.propoe_lance(leilao=leilao, valor=0.00)
