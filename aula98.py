# pasta é um package/pacote python com vários módulos (cada arquivo python é chamado de módulo)
import importlib

import aula98_m

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m)
    print(i)

print('Fim')