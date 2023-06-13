"""from log import LogPrintMixIn, LogFileMixIn



lp = LogPrintMixIn()
lp.log_error('oi')
lp.log_success('Que legal')
lf = LogFileMixIn()
lf.log_error('qualquer coisa')
lf.log_success('Que legal')"""

from eletronico import Smartphone

cel = Smartphone('nokia')
iphone = Smartphone('iphone')
cel.ligar()
cel.desligar()