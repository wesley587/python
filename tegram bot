import requests
import json
import os
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
search = False
url = False
option = Options()
option.headless = True
driver = webdriver.Firefox(executable_path='C://geckodriver.exe', options=option)
print('selenium passou')
cmd = ['/search', '/url', '/helper']
linesep = os.linesep

class TelegramBot:
    def __init__(self):
        token = '1447386898:AAGeNzBtrbLMn2MXAxoi1L0cS0kKDXxo0bg'
        self.url_base = f'http://api.telegram.org/bot{token}/'

    def iniciar(self):
        update_id = None
        while True:
            att = self.obter_msg(update_id)
            msgs = att['result']
            if msgs:
                for msg in msgs:
                    update_id = msg['update_id']
                    chat_id = msg['message']['from']['id']
                    primeira = msg['message']['message_id'] == 1
                    resp = self.criar_resp(msg, primeira)
                    print(resp)
                    self.responder(resp, chat_id)

    def obter_msg(self, update_id):
        link_req = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_req = f'{link_req}&offset={update_id + 1}'
        resul = requests.get(link_req)
        return json.loads(resul.content)

    def criar_resp(self, mensagem, primeira_ou_n):
        mensagem = mensagem['message']['text']
        if primeira_ou_n or mensagem == '/start':
            return f'''ola, bem vindo ao bot da pesquisa, digite um comando {os.linesep}/search {os.linesep}/url'''
        if '/' in mensagem and not url and not search:
            return self.comandos(mensagem)
        if search:
            return self.search(mensagem)
        if url:
            return self.cmd_url(mensagem)
        return 'ola, bem vindo'

    def comandos(self, comando):
        if comando not in cmd:
            return f'commando n existe tente algum desses {os.linesep}{cmd}'
        else:
            if comando == '/search':
                global search
                search = True
                return 'qual é o tema da pesquisa? '
            if comando == '/url':
                global url
                url = True
                return 'passe a url do video pra mim fazer a busca:'

    def cmd_url(self, busca):
        global url
        url = False
        driver.get(busca)
        sleep(5)
        parser = driver.find_element_by_xpath('//span[@class="view-count style-scope yt-view-count-renderer"]')
        contagem_v = parser.get_attribute('innerHTML')
        v = contagem_v.split(' ')
        valor = str(v[0])
        valor = valor.replace('.', '')
        valor = int(valor)
        Minimo = Maximo = atual_min = atual_max = 0
        quant = {10000000: {'minimo': 10000, 'maximo': 190000}, 1000000: {'minimo': 1000, 'maximo': 19000},
                 100000: {'minimo': 100, 'maximo': 1900}, 10000: {'minimo': 10, 'maximo': 190},
                 1000: {'minimo': 1, 'maximo': 19}}
        contagem = valor
        for key, values in quant.items():
            if contagem >= key:
                for k, v in values.items():
                    if k == 'minimo':
                        atual_min = v
                    else:
                        atual_max = v
                while contagem >= key:
                    contagem -= key
                    Maximo += atual_max
                    Minimo += atual_min
        sleep(3)
        title = driver.find_element_by_xpath('//h1[@class="title style-scope ytd-video-primary-info-renderer"]//yt-formatted-string[@class="style-scope ytd-video-primary-info-renderer"]')
        t = title.get_attribute('innerHTML')
        views = driver.find_element_by_xpath('//span[@class="view-count style-scope yt-view-count-renderer"]')
        v = views.get_attribute('innerHTML')
        nome_do_canal = driver.find_element_by_xpath(
            '//yt-formatted-string[@id="text"]//a[@class="yt-simple-endpoint style-scope yt-formatted-string"]')
        n = nome_do_canal.get_attribute('innerHTML')
        like = driver.find_elements_by_xpath(
            '//a[@class="yt-simple-endpoint style-scope ytd-toggle-button-renderer"]//yt-formatted-string[@id="text"]')
        sleep(5)
        count = pos = neg = 0
        for x in like:
            if count <= 1:
                por = ''
                parser = x.get_attribute('innerHTML')
                values = parser.split('&')
                value = values[0]
                if len(values) > 1:
                    por = values[1].split(';')
                if ',' in value:
                    value = value.replace(',', '')
                if value.isdigit():
                    print(value)
                    if por == 'mil':
                        value += '000'
                    value = int(value)
                    if count == 0:
                        pos = value
                    else:
                        neg = value
            count += 1

        tot = pos + neg
        maior = (pos / tot) * 100
        menor = 100 - maior
        maior = f'{maior:.2f}'
        menor = f'{menor:.2f}'
        return [f'views:{v}', f'canal:{n}', f'titulo:{t}', f'faturamneto esperado R${Minimo} e R${Maximo} porcentagem: {maior} gostaram {menor} n gostaram', ' ']

    def search(self, tema):
        global search
        search = False
        driver.get(f'https://www.youtube.com/results?search_query={tema}&sp=CAI%253D')
        t = driver.find_element_by_xpath('//ytd-item-section-renderer[@class="style-scope ytd-section-list-renderer"]')
        HTML = t.get_attribute('outerHTML')
        soup = BeautifulSoup(HTML, 'html.parser')
        teste = soup.find_all('a', {'id': 'video-title'})
        urls = list()
        for x in teste:
            urls.append('https://youtube.com/' + x['href'])
        return urls

    def responder(self, resposta, chat_id):
        if type(resposta) == list:
            count = 0
            for x in resposta:
                if count < 10:
                    link_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={x}'
                    requests.get(link_envio)
                count += 1
        else:
            link_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
            requests.get(link_envio)


bot = TelegramBot()
bot.iniciar()
