from datetime import datetime, timedelta

from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy

from .models import Things


@shared_task()
def send_news_email_task(things_of_last_week, user: dict):
    message_text = f'Hello, {user["first_name"]}! See all our offers from last week!\n'
    for things in things_of_last_week:
        msg_chunk = f"""New things:\n {things['name']}, Release date: {things['created_at']}, Price: {things['price']}
        More details: {reverse('product:detail', args=[things['id']])}
        """
        message_text += msg_chunk
        send_mail(
            "Weekly news",
            message_text,
            "sitestock@gmail.com",
            [user["email"]],
            fail_silently=False,
        )


@shared_task()
def weekly_newsletter():
    all_users = list(User.objects.filter(is_staff=False).values())
    all_things_of_last_week = list(
        Things.objects.filter(
            created_at__gte=datetime.today() - timedelta(days=7)
        ).values()
    )
    for user in all_users:
        send_news_email_task.delay(all_things_of_last_week, user)
