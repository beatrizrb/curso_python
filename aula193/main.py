from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# esse abaixo faz a espera
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/


# voce usa o selenium para automatizar processos 
# ou criar testes 


ROOT_FOLDER = Path(__file__).parent 
# pegando a cima o caminho da pasta aula193

CHROMEDRIVER_EXEC = ROOT_FOLDER/'drivers'/ 'chromedriver'
# as options sao as configurações que fornece para o chrome
"""chrome_options = webdriver.ChromeOptions()
# qual vai ser o serviço que vai utilizar o chrome
chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))
# embaixo é o navegador em si
chrome_browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_options,
)
# pode adicionar opções na configuração assim:
# headless para nao abrir a interface
#chrome_options.add_argument('--headless')
# da forma chrome_browser.get('http://www.google.com.br')
# ele abre e fecha o navegador rapido
chrome_browser.get('http://www.google.com.br')
# por isso adiciona o time.sleep para ele ficar aberto
# 30 segundos
sleep(30)"""

# fazendo uma função para abrir o navegador:

def make_chrome_browser(*options:str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))
    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )
    return chrome_browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # Example
    options = ('--disable-gpu', '--no-sandbox')
    browser = make_chrome_browser(*options)
    browser.get('https://www.google.com.br')
    # Espere para encontrar o input
    # until ate a condição esperada que é ate o elemento esteja
    # presente na tela
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        ))
    # se o input for encontrado ele vai digitar 
    # isso na tela para mim
    search_input.send_keys('Hello, World!')

    sleep(10)

