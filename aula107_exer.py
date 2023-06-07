

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]


#l3 = list(zip(l1, l2))

#lista = [list(a)[0] + list(a)[1]
     #     for a in l3]

lista = [x + y for x, y in zip(l1, l2)]
#assim desempacota
#for a in l3:
 #   list(a)
 #   lista.append(a[0]+ a[1])
print(lista)
