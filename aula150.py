# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

# decorator simplesmente atribuem uma nova funcionalidade para a função
# abaixo deles
@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
        #acima é uma pausa no meio do arquivo para retornar abaixo e executar
        # o corpo do with
        # depois do with ele fecha
    except Exception as e:
        print('Ocorreu erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()


with my_open('aula150.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)