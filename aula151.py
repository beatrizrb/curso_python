# Funções decoradoras e decoradores com classes

def meu_repr(self):
    print('estou mudando o metodo')
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

def adiciona_repr(cls):
    # funções decoradoras recebem a classe
    print('comecei aqui')
    print()
    cls.__repr__ = meu_repr
    print('terminei de mudar')
    return cls


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
#print(portugal)

#print(terra)
#print(marte)
