"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
 pop remove o ultimo valor da lista
 append adiciona o valor no final da lista
 clear - limpa a lista
 insert - adiciona item num indice especifico
 todos os outros elementos da lista sao colocados pra frente
 extend - nao retorna nada, adiciona a lista b em lista a, modificando 
 a variavel lista a
 .copy - retorna uma cópia da lista para uma nova variavel
 de forma a que se possa modificar essa variavel sem afetar a original
 e vice versa 
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3) # o pop retorna o valor retirado, 
# com on numero no pop, é o indice para remover o objeto da lista
print(lista, 'Removido,', ultimo_valor)