# copy, sorted, produtos.sort
import copy
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

#produtos1 = [a.items() for a in produtos]

#for a in produtos:
    #print(a['preco']*1.1)
    #a['preco'] = a['preco']*1.1
novos_produtos = [{**p, 'preco' : round(p['preco']*1.1, 2)} # expandindo e criar a nova chave 
            for p in copy.deepcopy(produtos)]
#print(novos_produtos)
#novos_produtos = copy.deepcopy(produtos) # gerando copia profunda

produtos_ordenados_por_nome = sorted(copy.deepcopy(novos_produtos), key=lambda item: item['nome'], reverse=True)
# sempre que for alterar algum dado mutavel, faço primeiro a cópia e depois a alteração se nao vocep pode estar alterando os dados originais
print(*produtos_ordenados_por_nome, sep='\n')
#produtos_ordenados_por_nome = copy.deepcopy(ordenado)

produtos_ordenados_por_preco  = sorted(copy.deepcopy(produtos), key=lambda item: item['preco'])

#produtos_ordenados_por_preco = copy.deepcopy(numero)

#print(produtos_ordenados_por_nome, produtos_ordenados_por_preco, sep='\n ')

#print(novos_produtos.sort(reverse=True))
