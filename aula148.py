# __new__ e __init__ em classes Python
#  __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# é o new que cria o objeto e retorna o self para o init
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs):
        # esta criando abaixo a instancia, o new tem que retornar a instancia
        instancia = super().__new__(cls)
        print(instancia)
        return instancia

    def __init__(self, x):
        self.x = x
        print('Sou o init')

    def __repr__(self):
        return 'A()'


a = A(123)
print(a.x)