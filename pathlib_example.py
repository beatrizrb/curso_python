from pathlib import Path
from shutil import rmtree

caminho_do_projeto = Path()
print(caminho_do_projeto) #caminho relativo de onde está o arquivo
print(caminho_do_projeto.absolute()) # caminho absoluto

caminho_arquivo = Path(__file__)
#print(caminho_arquivo) # agora é o caminho com o arquivo
#print(caminho_arquivo.parent) # ve a pasta mae deste arquivo

# posso criar caminhos com esses objetos

ideais = caminho_arquivo.parent / 'novaidea'
#print(ideais)

# para pegar a home do sistema:

# print(Path.home())
#estou criando o caminho para um novo arquivo
arquivo = caminho_do_projeto/'arquivo.txt'
# abaixo estou criando o arquivo de fato com touch
arquivo.touch()
# para escrever no arquivo posso fazer o write_text()
arquivo.write_text('') # mas esse é o modo rapido de fazer coisas
# e nao da para usar mais de uma vez esse write_text
# para ler eu posso usar read_text()
#print(arquivo.read_text())
# para apagar o arquivo eu uso unlink
#arquivo.unlink()

# entao a melhor maneira é abaixo

with arquivo.open('a+') as file:
    file.write('Uma linha\n')
    file.write('Outra linha\n')

print(arquivo.read_text())

# criando diretorios com mkdir:
caminho_pasta = caminho_do_projeto/ 'oi'
print(caminho_pasta)
# esse parametro exist_ok quer dizer se existir a pasta ja, nao da erro
caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)
for i in range(10):
    file = subpasta /f'file_{i}.txt'
    file.touch()



# para saber se é um arquivo (retorna True ou False) usa .is_file()
# para saber se existe voce usa .exists()
# esse rmdir é para apagar a pasta se ela estiver vazia
# caminho_pasta.rmdir()
# para apagar pastas com conteudo, use rmtree
rmtree(caminho_pasta)