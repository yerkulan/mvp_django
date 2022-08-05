import requests
from .models import TeleSettings


def sendTelegram(name, phone):
    settings = TeleSettings.objects.get(pk=1)
    token = settings.tg_token
    chat_id = settings.tg_chat
    text = settings.tg_text
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    part_1 = text[0:text.find('{')]
    part_2 = text[text.find('}')+1:text.rfind('{')]
    part_3 = text[text.rfind('}'):-1]

    text_slice = part_1 + name + part_2 + phone + part_3

    req = requests.post(
        method, data={
            'chat_id': chat_id,
            'text': text_slice
        }
    )
