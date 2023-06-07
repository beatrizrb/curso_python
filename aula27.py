"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] (ínicio, fim e passo (de quanto em quanto vai pular caracter))
Obs.: a função len retorna a qtd 
de caracteres da str
contagem é diferente de indice
mundo tem 5 caracteres mas os indices começam a partir do 0
"""
variavel = 'Olá mundo'
print(variavel[4:]) #inicio até o final
print(variavel[1:-1:2]) #pega um pula outro
print(variavel[::-1]) # inverte
