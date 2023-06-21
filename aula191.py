# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

# http:// -> 80
# https:// -> 443 (na porta 443)
url = 'http://localhost:3000/'
# resposta do servidor abaixo através da requisição feita pelo requests pelo 
# metodo get
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json())
# abaixo voce pega o html em texto
print(response.text)