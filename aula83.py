# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}


(a1, a2), (b1, b2) = pessoa.items() # desempacotamento interno
#print(a1, a2)
#print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}
# esses 2 astericos indica que esta extraindo
# chave e valores do dicionario pessoa e dados_pessoa
print(pessoas_completa)
# args - argumentos não nomeados
# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

# com kwargs sempre usa 2 asteriscos (**)
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


#mostro_argumentos_nomeados(nome='Joana', qlq=123)
mostro_argumentos_nomeados(**pessoas_completa)
# em cima ele pega chave e valor - faz o desempacotamento
# do dicionario pessoas_completas
configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)