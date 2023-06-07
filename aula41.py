""" while/else 
Quando termina de rodar o while, roda o else
Se der um break no while, o else não é executado"""
string = 'Valorqualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')