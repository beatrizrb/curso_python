# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    # quando eu chamo o sinal de atribuição (=) em um atributo
    # estou chamando o metodo do setter
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    #esse é o getter (o que retorna)
    # property é um metodo que se comporta como uma propriedade (atributo)
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name + 'oi'


foo = Foo('Bar')
print(foo.name)
# foo significa para voce preencher com qualquer coisa que vier na sua cabeça