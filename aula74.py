"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar # aqui ele não executou a fução
# mas salvou ela na memoria com os argumentos


falar_bom_dia = criar_saudacao('Bom dia') 
# criou uma função que cria outra função
falar_boa_noite = criar_saudacao('Boa noite')
print(falar_bom_dia) 
print(falar_bom_dia('Bia')) # executou, deu o closure da função
#for nome in ['Maria', 'Joana', 'Luiz']:
 #   print(falar_bom_dia(nome))
#    print(falar_boa_noite(nome))