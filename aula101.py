# Exercício - Adiando execuções de funções

def soma(x, y):
    #def somareal(y):
    return x + y
    #return somareal

def multiplica(x, y):
    #def multiplicarreal(y):
    return x*y
    #return multiplicarreal

def executa(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

soma_com_cinco = executa(soma, 5)
multiplica_por_dez = executa(multiplica,10) 

print(multiplica_por_dez(2)) # o closure da função
print(soma_com_cinco(10))