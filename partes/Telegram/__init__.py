import json
import requests


def url_base():
    token = '1447386898:AAGeNzBtrbLMn2MXAxoi1L0cS0kKDXxo0bg'
    return f'http://api.telegram.org/bot{token}/'


def obter_msg(update_id):
    link_req = f'{url_base()}getUpdates?timeout=100'
    if update_id:
        link_req = f'{link_req}&offset={update_id + 1}'
    resul = requests.get(link_req)
    return json.loads(resul.content)

