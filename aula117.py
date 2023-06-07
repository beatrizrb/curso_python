# json é uma estrutura de dados criada para você transportar ou salvar dados
# a estrutura é similar aos dicionarios do python

import json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula117.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )
    # dump é no arquivo
    # dumps é numa string
    # ensure_ascii = False para manter os acentos e caracteres certos
    # indent deixa o dicionario formatado
    # convertendo aqui um dicionario em json para salvar esses dados
with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo) # load carrega o arquivo
    # print(pessoa)
    print(type(pessoa))
    print(pessoa['nome'])
    # conversão de volta dos dados