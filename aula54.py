"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros
de índices inexistes na lista.
"""

lista =[]

while True:
    opcao = input('[i]nserir [a]pagar [l]istar')
    if opcao == 'l':
        for indice, item in enumerate(lista):
            print(indice, item)
    elif opcao == 'i':
        valor = input('Escolha o valor para adicionar: ')
        lista.append(valor)
    try:
        if opcao == 'a':
            indice = int(input('Escolha o índice para apagar: '))
            lista.pop(indice)
    except:
        print('Não foi possível apagar esse indice.')
        

