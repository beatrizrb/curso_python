"""
Introdução ao empacotamento e desempacotamento
"""
# *resto vai pegar todos os valores que restarem
# numa variavel chamaada resto que vai ser uma lista
# quando nao vou usar uma variavel, em vez de chamar de resto
# é convenção chamar de _
# os _ mostra que voce está ignorando os valores
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)