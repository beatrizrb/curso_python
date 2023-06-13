# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print(f'Email: enviando - {self.mensagem}')
        return False

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print(f'SMS: enviando - {self.mensagem}')
        return True

n = NotificacaoSMS('Testando')
n.enviar()
# eu sinalizo aqui embaixo que o argumento deve ser do tipo Notificacao
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação não enviada')

# polimorfismo ocorre aqui porque eu posso passar Notificacao
# Notificação Email e NOtificacaoSMS
notificacao_email = NotificacaoEmail('Oi')
notificar(notificacao_email)
notificacao_sms = NotificacaoSMS('testando sms')
notificar(notificacao_sms)

        

