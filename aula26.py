"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.') # no centro
print(f'{1000.6546845612418454:.2f}')
print(f'{1000.6546845612418454:,.2f}') #separa a milhar por ,
print(f'{1000.6546845612418454:+,.2f}') # + indica para aparecer o + quando for positivo
print(f'{1000.6546845612418454:0=+10,.2f}') #preenche com 10 espaços à esquerda
