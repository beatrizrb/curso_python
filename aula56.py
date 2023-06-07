"""
split e join com list e str
split - divide uma string  em(list)
(se nao passar nenhum argumento
ele vai dividir a partir dos espaços)
join - une uma string
strip - corta os espaços do começo e do fim da string
rstrip - corta espaço da direita
lstrip - corta espaço da esquerda
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
print(lista_frases)
frases_unidas = ', '.join(lista_frases)
# o que vem antes do .join é o separador
print(frases_unidas)
print(type(frases_unidas))