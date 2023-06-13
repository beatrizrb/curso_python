# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno


# string = MinhaString('Luiz')
# print(string.upper())

class A(object):
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    # A é a superclass
    # para usar um metodo de A sem sobrescrever com B,
    # tem que chamar o super
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        # estou sobrepondo o init do A, e chamo embaixo o super
        # para rodar o init do A para nao perder o atributo "atributo"
        super().__init__(atributo)
        self.outra_coisa = outra_coisa
        # estou adicionando outro atributo aqui agora
        # C vai ter esses 2 atributos

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        # print('EI, burlei o sistema.')
        super().__init__(*args, **kwargs) 
        print('09'*40)
        print(*args, **kwargs, sep='oioioioi')

    def metodo(self):
        # super().metodo()  # B
        # super(B, self).metodo()  # A
        # super(A, self).metodo()  # object
        super(B, self).metodo() # mesma coisa de chamar assim embaixo
        # A.metodo(self)
        B.metodo(self)
        print('C')


# print(C.mro()) # method resolution order para saber a ordem das classes
# print(B.mro())
# print(A.mro())
c = C('Atributo', 'Qualquer')
# print(c.atributo)
# print(c.outra_coisa)
c.metodo()
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()