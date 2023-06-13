# Se eu estou criando uma classe, estou criando o meu proprio tipo
# Abstração
# Herança - é um
# Log

from pathlib import Path
# pegar o caminho absoluto do arquivo pode ser
# Path(__file__).parent
LOG_FILE = Path(__file__).parent/'log.txt'

class Log:
    def _log (self, msg):
        # essa é a abstração
        # não quero que alguem use essa classe diretamente
        # quando aparece isso é porque normalmente
        # a pessoa quer que use a subclasse e não a superclasse
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg1):
        return self._log(f'Error: {msg1}')

    def log_success(self, msg1):
        return self._log(f'Success: {msg1}')
    
class LogFileMixIn(Log):
    # o nome Mixin sinaliza que é para voce adicionar
    # funcionalidades na herança multipla
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

# colocando um _ indicando que não é para usar, modo privado
class LogPrintMixIn(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
    
if __name__ == '__main__':
    lp = LogPrintMixIn()
    lp.log_error('oi')
    lp.log_success('Que legal')
    lf = LogFileMixIn()
    lf.log_error('qualquer coisa')
    lf.log_success('Que legal')
    