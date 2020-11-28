from partes.responder import resp
from partes.Telegram import obter_msg
from partes.responder import criar_resp


def iniciar(driver):
    update_id = None
    while True:
        att = obter_msg(update_id)
        msgs = att['result']
        if msgs:
            for msg in msgs:
                print(msg)
                texto = msg['message']['text']
                update_id = msg['update_id']
                chat_id = msg['message']['from']['id']
                primeira = msg['message']['message_id'] == 1
                resposta = criar_resp(texto, driver, chat_id, update_id, primeira)
                resp(resposta, chat_id)
