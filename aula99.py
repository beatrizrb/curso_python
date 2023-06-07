# cria um arquivo na raiz que vai ser o main, a partir
# dele voce importa outras coisas
#from sys import path
# PACKAGES PODEM SER INICIALIZADOS COM ARQUIVOS __init__.py (ele é executado assim que o modulo é executado)
# qualquer coisa que for importada do package esse init é executado
# o package passa a se comportar como modulo
#from aula_99_package import modulo
#from aula99_package.modulo import *
#print(*path, sep='\n')
#print(__name__)
#print(soma_do_modulo(8, 2))

# from sys import path
# https://stackoverflow.com/questions/2386714/why-is-import-bad

# import aula99_package.modulo
# from aula99_package import modulo
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)
#from aula99_package.modulo import fala_oi, soma_do_modulo
# from aula99_package.modulo import fala_oi, soma_do_modulo

#print(__name__)
#fala_oi()
# print(__name__)
# fala_oi()

from aula99_package import falar_oi, soma_do_modulo, nova_variavel

print(soma_do_modulo(2, 3))
falar_oi()
print(nova_variavel)