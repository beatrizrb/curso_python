# um iterable (iteravel) é uma coisa que pode fazer um loop em cima
# por exemplo posso fazer um for em uma lista

lista = [1 , 2, 3]

# for numero in lista:
#   print(numero)

# todo iterable tem o metodo __iter__()
# a lista tem este metodo? Verificamos com dir
# print('__iter__' in dir(lista)) # sim, ela tem, então ela é um iterable
# lista nao tem o metodo __next__ por isso nao é iterator

# a sua lista não é um iterator
# quando rodamos __iter__ ele retorna um iterator
# abaixo num1 vira um iterator
i_num = lista.__iter__() # esse é o iterator da nossa lista
# como é feio ficar chamando dunder method
# em vez de chamar __iter__()
# podemos chamar iter()

i_num = iter(lista)

print(i_num)
print()
print(dir(i_num))
# quando printamos o dir para ver os metodos disponiveis do iterador
# vemos que alem __next__ ele tem __iter__, porque todo iterator 
# é iterable (tem o metodo __iter__/ iter())
# no caso do metodo __iter__ do iterator, ele retorna ele mesmo "self"
# print(iter(i_num))
#print(next(i_num))
#print(next(i_num))
#print(next(i_num))
# saber disso é interessante porque podemos adicionar esses metodos nas 
# nossas classes e as tornar iteraveis/iterable também

# por exemplo vou tentar criar uma classe que age que nem o range()


class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return self # ele vai retornar ele mesmo porque vou definir 
    # embaixo um metodo __next__

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current
    
# abaixo é um generator que é um iterator sem voce precisar definir iter e next
# ele defini isso automaticamente
# quando rodar num for loop com isso tbm
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


nums = my_range(1,10)
print(next(nums))
print(next(nums))

# essa classe acima é iteravel/iterable porque podemos usar num for loop
# essa classe também é um iterator porque tem o metodo __next__
# "an iterator has a state where it knows where it is during iteration
# and iterators also know how to get their next value
# They get their next value with method __next__"
