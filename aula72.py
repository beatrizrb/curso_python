# Exercicios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
#Retorne o total para uma variável e mostre o valor
# da variável
# exemplo multiplica 1*2*3
def multiplicar(*args):
    total = 1
    #lista = list(args)
    for x in args:
        print(f'{x=}{total=}')
        total *=  x
    return total

numeros = 4, 2, 3
print(multiplicar(*numeros))

# Crie uma função fala se o número é par ou ímpar.
# Retorne se o número é par ou ímpar
def pi(num):
    resultado = ''
    if num % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Ímpar'
    return resultado

print(pi(7))

