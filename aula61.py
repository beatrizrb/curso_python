"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

"""cpf = '746.824.890-70'
cpfsemnada = ''
listamultiplicacao =[]
for i in cpf:
    if i != '.' and i != '-':
        cpfsemnada += i
# coletar as multiplicações
for i in range(10, 1, -1):
    #print(i)
    multiplicao = int(cpfsemnada[len(cpfsemnada) - i - 1]) * i
    listamultiplicacao.append(multiplicao)
    
# coletar soma
soma = 0
for a in listamultiplicacao:
    soma+=a

# multiplicar por 10 e Obter o resto da divisão da conta anterior por 11

somanova = soma * 10
restosoma = somanova % 11
restosoma = restosoma if restosoma <= 9 else 0
print(restosoma)"""
#solução do professor:
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0   
print(digito_1)
