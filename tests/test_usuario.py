from src.leilao.dominio import Leilao, Usuario


def test_subtrair_valor_carteira_lance_bem_sucedido():
    usuario = Usuario(nome="Usuário de teste", valor_carteira=500.00)
    leilao = Leilao(descricao="Venda de celular")
    usuario.propoe_lance(leilao=leilao, valor=200.00)
    assert usuario.carteira == 300.00