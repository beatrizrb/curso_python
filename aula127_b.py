import json
from aula127_a import Taylor, fazer_dump

#fazer_dump()

with open('json127.json', 'r') as file:
    a = json.load(file)
    a1 = Taylor(**a[0])
    a2 = Taylor(**a[1])
    a3 = Taylor(**a[2])


print(a)


print(a)
print(a1.nome)
print(a1.ano)
print(a1.get_nota())
print(a2.nome)
print(a2.get_nota())

