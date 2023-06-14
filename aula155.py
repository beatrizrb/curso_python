# Metaclasses são o tipo das classes
# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# o tipo da sua instancia é a classe a partir da qual ela foi criada
# o tipo da sua classe é chamado de type
# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe
# Sua classe é uma instância de type (type é uma metaclass)
# type('Name', (Bases,), __dict__)
#
# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instância)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execução
#
# Métodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)
#
# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# — Tim Peters (CPython Core Developer)

# object acima
# class Foo:
#     ...

# estou criando uma classe com type chamada de Foo
# na tupla é as heranças da classe
# terceiro parametro é o dict da classe em si
Foo = type('Foo', (object,), {})
f = Foo()
# print(isinstance(f, Foo))
#print(type(f))
#print(type(Foo))
# toda metaclass precisa herdar de type
def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'

# basicamente voce pode executar tarefas antes da criação da classe em si
class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        # cria a classe e retorna a classe
        # no metodo new nao consegue ver a instancia, acessar self.
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = meu_repr

        if 'falar' not in cls.__dict__ or \
                not callable(cls.__dict__['falar']):
                # acima estou verificando se existe o metodo .falar() no dict da classe
            raise NotImplementedError('Implemente falar')

        return cls

    def __call__(cls, *args, **kwargs):
        # quando defino o call, estou falando que a instancia da classe se torna executavel
        # quando eu defino o call na metaclass, estou falando dos parentheses na chamada classe
        # como em Pessoa('MArcos')
        instancia = super().__call__(*args, **kwargs)

        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o attr nome')

        return instancia

# Pessoa é uma instancia de Meta
class Pessoa(metaclass=Meta):
    # falar = 123

    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome

    def falar(self):
        print('FALANDO...')

# p1 é uma instancia de Pessoa
p1 = Pessoa('Luiz')
p1.falar()