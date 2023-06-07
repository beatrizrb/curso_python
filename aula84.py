# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]

lista= [b * 3 for b in 'Beatriz']
print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} # 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(novos_produtos)
#print(*novos_produtos, sep='\n')
# mapeamento é voce pegar um dado, transformar e jogar em outra lista que vai ter o mesmo tamanho da onde voce tirou os dados
# filtro quer dizer que voce pode ou nao incluir esse dado na sua lista
# lista = [n for n in range(10) if n < 5] # o que vem a esquerda do for é mapeamento
# e a direita é filtro
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    #if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
    if (produto['preco'] >= 20)
]
p(novos_produtos)