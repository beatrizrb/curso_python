# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula179.csv'

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    #print(next(leitor))
    #print(next(leitor))
    #print(next(leitor))

    for linha in leitor:
        print(linha["Nome"], linha["Idade"], linha["Endereco"])
        #print(linha['Nome'], linha['Idade'], linha['Endereço'])

# with open(CAMINHO_CSV, 'r') as arquivo:
#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         print(linha)