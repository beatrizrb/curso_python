# Variáveis livres + nonlocal (locals, globals)
# o locals te fala quais variaveis sao locais
# print(globals())
# def fora(x):
#     a = x #a é uma variavel livre porque ela nao esta definida dentro do escopo
# da função dentro

#     def dentro():
#         # print(locals())

#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())
def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final # voce coloca isso para conseguir
        # alterar o valor da variavel que nao foi definida nesse escopo
        # "variavel livre" . Esse nonlocal vai lembrar o valor
        # da variavel
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c('e')
print(final)