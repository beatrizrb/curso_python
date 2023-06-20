# Enviando E-mails SMTP com Python
import os
import pathlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage # para mandar imagem
from string import Template

from dotenv import load_dotenv  # type: ignore

load_dotenv()

# Caminho arquivo HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula185.html'

# Dados do remetente e destinatário
# estou enviando o email para o mesmo email
remetente = os.getenv('FROM_EMAIL', '')
#destinatario = remetente
destinatario = os.getenv('TO_EMAIL', '')

# Configurações SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto
with open(CAMINHO_HTML, 'r') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Marcos')

# Transformar nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# adicionando imagem abaixo
with open('/home/beatriz/Downloads/venus-cat1.jpg', 'rb') as f:
        img_data = f.read()
image = MIMEImage(img_data, name=os.path.basename('/home/beatriz/Downloads/venus-cat1.jpg'))
mime_multipart.attach(image)

# Envia o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    # abaixo significa extended hello, inicia a conexao com o servidor
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com  sucesso!')