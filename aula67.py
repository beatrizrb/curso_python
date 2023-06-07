"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
da mesma forma com argumentos posicionais e nomeados
toda vez que definir um parametro com valor padrao
tem que definir os parametros depois dele com valores
padrao tambem
"""


def soma(x, y, z=None): # o interessante de usar
    #None aqui é que mesmo se 0 for enviado, ele
    # que é um valor falsy, será aceito pois é diferente
    #de None
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)