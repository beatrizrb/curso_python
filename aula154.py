# Classes decoradoras (Decorator classes)
# decorador fica com letra maiuscula, pois indica que é uma classe
# decorando a função

from typing import Any


class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador
    # o que vem em args e kwargs são os argumentos passados para a função soma    
    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado  = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna


@Multiplicar(2)
def soma(x,y):
    return x+y

a = soma(2,2)
print(a)