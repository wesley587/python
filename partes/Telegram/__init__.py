import json
import requests
import yaml

with open("Token.yml") as file: # Change path
    parser = yaml.load(file, Loader=yaml.FullLoader)
    for x in parser.values():
        Token = x
file.close()


def url_base():
    token = Token
    return f'http://api.telegram.org/bot{token}/'


def obter_msg(update_id):
    link_req = f'{url_base()}getUpdates?timeout=100'
    if update_id:
        link_req = f'{link_req}&offset={update_id + 1}'
    resul = requests.get(link_req)
    return json.loads(resul.content)

