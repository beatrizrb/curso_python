# Exercício - sistema de perguntas e respostas

perguntas = [{
    'Pergunta': 'Quanto é 2+2?',
    'Opções' : ['1', '3', '4', '5'],
    'Resposta': '4',
},
{
    'Pergunta' : 'Quanto é 5*5?',
    'Opções' : ['25', '55', '10', '51'],
    'Resposta' : '25',
},
{
    'Pergunta' : 'Quanto é 10/2?',
    'Opções' : ['4', '5', '2', '1'],
    'Resposta' : '5',
},
]

acertos = 0
for b in perguntas:
    print(f"Pergunta: {b['Pergunta']}")
    print()

    print(f'Opções: ')
    for i, valor in enumerate(b['Opções']):
        print(str(i) +')', valor)
    print()

    resposta = input(f'Escolha uma opção: ')
    acertou = False
    escolha_int = None

    if resposta.isdigit():
        escolha_int = int(resposta)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < len(b['Opções']):
            if b['Opções'][escolha_int] == b['Resposta']:
                acertou = True
    print()
    if acertou:
        acertos += 1
        print('Acertou')
    else:
        print('Errou')
    
    print()
    """if b['Opções'][escolha_int] == b['Resposta']:
        print('Acertou!')
        acertos += 1
    else:
        print('Errou')"""
print(f'Você acertou {acertos} de 3 perguntas.')
   

   