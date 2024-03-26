import datetime
import json

import requests
from django.conf import settings


def send_message(text, chat_id):
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_TOKEN

    requests.post(
        url=f"{URL}{TOKEN}/sendMessage",
        data={
            "chat_id": chat_id,
            "text": text
        }
    )
