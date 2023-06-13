# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
# estou falando acima que cliente que herda de pessoa (desde animal) também herda
# de filelog
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar (que vai ter em A, B e C)
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Se D quiser usar o metodo falar ele tem que decidir aonde vai encontrar
# esse metodo, o python usa C3 superclass para definir isso
# Para usar determinado metodo de classes acima, o Python vai ter que decidir
# qual caminho seguir
# Python 3 usa C3 superclass linearization
# para gerar o mro.
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)

class A:
    ...

    def quem_sou(self):
        print('A')


class B(A):
    ...

    # def quem_sou(self):
    #     print('B')


class C(A):
    ...

    def quem_sou(self):
        print('C')


class D(B, C):
    ...

    def quem_sou(self):
        print('D')


d = D()
d.quem_sou()
# print(D.__mro__)
print(D.mro())