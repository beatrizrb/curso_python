# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# namedtuples sao interessantes quando voce quer registrar dados e atributos
# mas sem precisar usar metodos ou alterar dados
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm
# from collections import namedtuple da mesma maneira que abaixo
#Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#     defaults=['VALOR', 'NAIPE']
# )
from typing import NamedTuple

# aqui esta criando uma namedtuple
class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'


# Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#     defaults=['VALOR', 'NAIPE']
# )
as_espadas = Carta('A')

print(as_espadas._asdict())
print(as_espadas)
print(as_espadas[0])
print(as_espadas.valor)
print(as_espadas[1])
print(as_espadas.naipe)

print()
print(as_espadas._fields)
print(as_espadas._field_defaults)


for valor in as_espadas:
    print(valor)