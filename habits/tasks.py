from datetime import datetime

import requests
from celery import shared_task
from django.conf import settings

from habits.models import Habit


@shared_task
def send_reminder_about_habit():
    """
    Отправка пользователю в Телеграм напоминания о привычке
    """
    URL = "https://api.telegram.org/bot"
    TOKEN = settings.TELEGRAM_TOKEN

    time_now = datetime.now().time()
    data_now = datetime.now().date()
    habits_to_send = Habit.objects.filter(time=time_now, date=data_now)

    for habit in habits_to_send:
        chat_id = habit.owner.telegram_id
        text = f"Я сделаю {habit.action} в {habit.time} в {habit.place}"
        requests.post(
            url=f"{URL}{TOKEN}/sendMessage",
            data={
                'chat_id': chat_id,
                'text': text,
            }
        )
