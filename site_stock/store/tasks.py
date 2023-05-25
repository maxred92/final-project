from time import sleep

from celery import shared_task
from django.core.mail import send_mail

@shared_task()
def send_feedback_email_task(email_address, message):
    """ Function for composing a feedback message """
    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you!",
        "sitestock@gmail.com",
        [email_address],
        fail_silently=False,
    )
