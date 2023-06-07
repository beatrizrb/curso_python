frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'
# Qual letra apareceu mais vezes na frase?
i = 0
qtd_apareceu_maisvezes = 0
letra_que_apareceumaisvezes = ''
while i < len(frase): #iteração
    letra_atual = frase[i]
    if letra_atual ==' ':
        i += 1
        continue
    quantas_vezes_apareceu = frase.count(letra_atual)

    if qtd_apareceu_maisvezes < quantas_vezes_apareceu:
        qtd_apareceu_maisvezes = quantas_vezes_apareceu
        letra_que_apareceumaisvezes = letra_atual
    
    i += 1
print(f'A letra que apareceu mais vezes foi '
          f'{letra_que_apareceumaisvezes} que apareceu '
          f'{qtd_apareceu_maisvezes} vezes.')

