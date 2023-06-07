import sys
# generator sao funções que sabem pausar
# todo generator é um iterator também
# mas um iterator não é um generator
# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)
print(next(iterator))
  # tem __iter__ e __next__
lista = [n for n in range(100)]
generator = (n for n in range(100))
# os dois tem os mesmos valores, mas a lista esta na memoria
# e o generator nao, está esperando
print(sys.getsizeof(lista)) # ver o tamanho na memoria
print(sys.getsizeof(generator)) # esta pausado na função porque
# nunca pediu next para ele

print(next(generator))
print(next(generator))
print(next(generator)) # aqui ele entrega os valores
print(next(generator))

# vantagens da lista:
# como ela esta inteira na memoria, posso acessa-la
# indice por indice, da para saber o tamanho dela
# o generator nao da para saber tamanho, indice

for n in generator:
     print(n)