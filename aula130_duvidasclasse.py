# method vs @classmethod vs @staticmethod
# method - self, método de instância
# diferença entre method e classmethod é que o method
# recebe a propria instancia (self) e o outro recebe
# a propria classe (cls)
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

"""
O self é usado em métodos de instância para referenciar o objeto atual da classe. 
Ele é necessário para que você possa acessar e modificar os atributos do objeto durante a execução do método. 
O self permite que os métodos de instância acessem e modifiquem os atributos de instância da classe, enquanto @classmethod e @staticmethod 
não podem fazer isso diretamente.

Você pode usar @classmethod para criar métodos que afetam a classe em si, em vez de instâncias individuais. 
Esse tipo de método é útil para criar instâncias de classe, aplicar alterações a todas as instâncias da classe e outras tarefas 
que envolvem a classe como um todo.

O @staticmethod é semelhante ao @classmethod, mas não requer acesso à classe ou aos atributos da instância. 
Em vez disso, ele é usado quando você tem uma função que está relacionada à classe, mas não precisa de acesso a nenhum atributo de 
instância ou classe.

Quanto à definição de atributos em __init__, é uma boa prática definir todos os atributos de instância necessários na inicialização da classe.
No entanto, se você não definir todos os atributos em __init__, poderá defini-los posteriormente com self. Mas é importante ter em mente que,
se você não definir um atributo de instância em __init__ ou posteriormente em algum método, ele não existirá e você não poderá usá-lo.
"""
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
# toda vez que eu tiver que usar self, esse metodo é de 
# instancia
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print('LOG:', msg)


def connection_log(msg):
    print('LOG:', msg)


# c1 = Connection()
c1 = Connection.create_with_auth('luiz', '1234')
# c1.set_user('luiz')
# c1.set_password('123')
print(Connection.log('Essa é a mensagem de log'))
print(c1.user)
print(c1.password)