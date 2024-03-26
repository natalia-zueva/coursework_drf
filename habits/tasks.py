from datetime import datetime

import requests
from celery import shared_task
from django.conf import settings

from habits.models import Habit
from habits.services import send_message


@shared_task
def send_reminder_about_habit():
    """
    Отправка пользователю в Телеграм напоминания о привычке
    """

    print("Send message")

    time_now = datetime.now().replace(second=0, microsecond=0)
    habits_to_send = Habit.objects.filter(time=time_now)

    for habit in habits_to_send:
        chat_id = habit.owner.telegram_id
        text = f"Я сделаю {habit.action} в {habit.time} в {habit.place}"
        send_message(chat_id, text)
