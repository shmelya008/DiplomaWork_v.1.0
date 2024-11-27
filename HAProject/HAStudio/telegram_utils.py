import urllib.request
import json
from django.template.loader import render_to_string
import os
from dotenv import load_dotenv
from .models import User

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

'''
Здесь я пока не до конца разобрался как сделать, чтобы передавать в шаблон
переменные, которые отправляются в Телеграм 
И как сделать так чтобы передавались переменные пользователя,
который в данный момент вошёл в свой профиль на сайте.
Буду работать над этим :)
'''


def get_html_message_from_template() -> str:
    user = User.objects.filter(id=21)
    return render_to_string('telegram_message.html', {
        'user': user
    })


def send_telegram_message(chat_id: str, report):
    # Используется метод sendMessage API Telegram
    api_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

    # Указываем в параметрах CHAT_ID и само сообщение
    input_data = json.dumps(
        {
            'chat_id': CHAT_ID,
            'text': get_html_message_from_template(),
            'parse_mode': "HTML"
        }
    ).encode()

    try:
        req = urllib.request.Request(
            url=api_url,
            data=input_data,
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req) as response:
            # Тут выводим ответ
            print(response.read().decode('utf-8'))

    except Exception as e:
        print(e)
