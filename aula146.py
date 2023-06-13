# desenvolvedores comunicam erros através de exceções (Exceptions)
# Normalmente não existe necessidade de fazer algo numa exceção
# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
# Levantando e tratando suas Exceptions (Exceções)
# Notas das exceptions em Python (add_notes, __notes__)
class MeuError(Exception):
    ...


class OutroError(Exception):
    ...


def levantar():
    # posso mandar varias coisas na exceção
    exception_ = MeuError('a', 'b', 'c')
    # consigo adicionar nota as exceções
    # mas só funciona com python 11
    exception_.add_note('Olha a nota 1')
    exception_.add_note('você errou isso')
    raise exception_

# isso abaixo se chama tratar exceções
# de forma que vai aparecer apenas o texto que voce formatou
try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    # aqui embaixo para voce ver o nome da classe que gerou
    # essa exceção
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar de novo')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Mais uma nota')
    # estou relançando a exceção (lançando uma exceçao a partir de uma exceção)
    raise exception_ from error