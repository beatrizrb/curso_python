# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# por exemplo str (classe) gera um novo objeto "luiz"
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
# criando uma nova classe (um molde que vai gerar novos objetos)

p1 = Pessoa('Luiz','Otávio') # gerando uma nova instancia da classe Pessoa
# quando falamos de dados dentro da classe, estamos falando de atributos
# ações/ funções executadas dentro da classe são chamadas de métodos
""" p1.nome = 'Luiz' # atributo nome
p1.sobrenome = 'Otávio' """ #atributo sobrenome

p2 = Pessoa('Maria', 'Joana') # criando uma nova instancia
""" p2.nome = 'Maria'
p2.sobrenome = 'Joana' """

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)