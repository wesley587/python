from partes.Telegram import url_base
from partes import comando
from partes import Telegram


def criar_resp(mensagem, driver,chat_id, update_id,  primeira_ou_n=False):
    if primeira_ou_n or mensagem == '/start':
        return f'''ola, bem vindo ao bot da pesquisa, digite um comando \n/search \n/url'''
    if '/' in mensagem:
        return comandos(mensagem, chat_id, driver, update_id)
    return 'ola, bem vindo'


def comandos(com, chat_id, driver, update_id):
    texto = ''
    cmd = ['/url', '/search']
    if com not in cmd:
        return f'commando n existe tente algum desses \n{cmd}'
    else:
        if com == '/search':
            for x in range(0, 2):
                if x == 0:
                    resp('qual o tema da ppesquisa?', chat_id)
                else:
                    att = Telegram.obter_msg(update_id)
                    msgs = att['result']
                    if msgs:
                        for msg in msgs:
                            texto = msg['message']['text']
                            update_id = msg['update_id']
                            chat_id = msg['message']['from']['id']
                            comando.search(texto, driver, chat_id)
        if com == '/url':
            for x in range(0, 2):
                if x == 0:
                    resp('passe a url:', chat_id)
                else:
                    att = Telegram.obter_msg(update_id)
                    msgs = att['result']
                    if msgs:
                        for msg in msgs:
                            texto = msg['message']['text']
                            update_id = msg['update_id']
                            chat_id = msg['message']['from']['id']
                            comando.cmd_url(texto, driver, chat_id)


def resp(resposta, chat_id):
    import requests
    if type(resposta) == list:
        count = 0
        for x in resposta:
            if count < 10:
                link_envio = f'{url_base()}sendMessage?chat_id={chat_id}&text={x}'
                requests.get(link_envio)
            count += 1
    else:
        link_envio = f'{url_base()}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_envio)
    return 'algo mais'
