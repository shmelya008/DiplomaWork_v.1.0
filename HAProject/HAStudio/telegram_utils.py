import urllib.request
import json
from django.conf import settings
from django.template import Template, Context
from django.template.loader import render_to_string
import sys
import os
from dotenv import load_dotenv
from .views import Report

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# def get_html_message(report):
#     html_template = Template(
#         """<a href="{{ report.url }}">{{ report.title }}</a>{{ report.content|truncatewords:30 }}"""
#         """<strong>Дата создания:</strong>{{ report.created_at|date:'SHORT_DATE_FORMAT' }}""")
#     return html_template.render(Context({'report': report}))

def get_html_message_from_template() -> str:
    report = Report.objects.all()
    return render_to_string('telegram_message.html', {
        'report': report
    })

def send_telegram_message(chat_id: str, report):
    # Используется метод sendMessage API Telegram
    # Обратите внимание , что мы тут используем BOT_TOKEN
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
            #Тут выводим ответ
            print(response.read().decode('utf-8'))

    except Exception as e:
        print(e)


# if __name__ == "__main__":
#     send_telegram_message()

