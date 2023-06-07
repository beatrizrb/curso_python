# primeiro exercicio

numero = input('Digite um número inteiro:')

try:
    #numero.isdigit()
    numeroint = int(numero)
    if numeroint %2 ==0:
        print(f'O número {numeroint} é par.')
    else:
        print(f'O número {numeroint} é ímpar.')
except:
    print(f'{numero} não é um número inteiro.')

#Segundo Exercicio
hora = input('Qual é a hora agora?')
#manha = 0<=hora<=11 
#tarde = 12<=hora<=17 
#noite = 18<=hora<=23 
try:
    hora = int(hora)
    manha = 0<=hora<=11 
    tarde = 12<=hora<=17 
    noite = 18<=hora<=23 
    if manha:
        print('Bom dia!')
    elif tarde:
        print('Boa tarde!')
    else:
        print('Boa noite!')
except:
    print('Por favor, digite apenas números inteiros.')

#Terceiro Exercicio
nome = input('Digite o seu primeiro nome')
curto = len(nome) <= 4
normal = len(nome)==5 or len(nome)==6
grande = len(nome) > 6

if curto:
    print(f'Seu nome é curto.')
elif normal:
    print(f'Seu nome é normal.')
else:
    print(f'Seu nome é muito grande.')
