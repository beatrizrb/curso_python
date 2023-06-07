# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy() # se fizer d2 = d1 isso indica que os dois apontam para o mesmo dicionario
# guardado na memoria, de forma que se alterar d2, altera automaticamente d1
# por isso se faz a cópia de forma se alterar d2, não alterar d1. esse .copy
# é uma cópia rasa, o que significa que tudo que for imutável vai ser copiado
# mas se você tiver uma lista por exemplo (valor mutável), essa cópia não é feita
# então os dois dicionarios vão apontar para a mesma lista na memória
# se você quiser copiar mesmo esses itens mutaveis, voce usa o método
# deepcopy da biblioteca copy (copy.deepcopy(dicionario))

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)