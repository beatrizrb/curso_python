# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, asdict, astuple, field, fields
# função field que voce usa para configurar os seus campos na dataclass
# fields te da informações sobre os seus campos

# aqui dentro eu defino apenas os atributos
# o init e repr ja estao definidos com esse decorador sem eu precisar
# fazer as funções
# init=False tira o init da dataclass, entao vou ter que definir o 
# meu proprio init
# o frozen congela a class, nao consegue mudar valores dela
# repr=False desativa o metodo repr
# @dataclass(init=False, frozen=True, repr=False, order=True):
# order=True permite que voce ordene uma lista com Instancias 
# da classe com sorted()
@dataclass
class Pessoa:
    # nao pode criar valor padrao de atributo com valor mutavel 
    # tipo listas
    # field pode tambem receber um valor padrao
    nome: str = field(default='Missing')
    idade: int = 0
    sobrenome: str = ''
    endereco: list[str] = field(default_factory=list)
    # toda vez que eu criar uma instancia sem endereço 
    # ele vai criar uma nova lista

    def __post_init__(self):
        # executado depois do init da dataclass
        # se desativar init da dataclass, ele não é executado
        # print('POST INIT')
        ...

    """@property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        print(sobrenome)
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)"""

if __name__ == '__main__':
    # p1 = Pessoa('Luiz', 30)
    # p2 = Pessoa('Luiz', 30)
    # print(p1)
    # esta definido tbm o metodo __eq__ por isso consigo 
    # comparar abaixo
    # print(p1 == p2)
    p1 = Pessoa('Luiz', 30, 'Otávio', ['Avenida do Cafe'])
    #p1.nome_completo = 'Maria Helena das Cruzes'
    # lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    # como nao passei o parametro order entao dataclass, posso criar
    # a minha propria ordem aqui com lambda
    # ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    # asdict converte a sua dataclass para um dicionario
    # astuple para uma tupla
    #print(asdict(p1))
    #print(astuple(p1))
    print(p1.endereco)
    print(fields(p1))