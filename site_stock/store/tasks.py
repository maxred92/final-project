from time import sleep

from celery import shared_task
from django.core.mail import send_mail

""" Running a task to send an email to the user who left the review """


@shared_task()
def send_feedback_email_task(email_address, message):
    """Sends an email when the feedback form has been submitted."""
    sleep(10)  # simulate expensive operation that freezes Django
    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you!",
        "sitestock@gmail.com",
        [email_address],
        fail_silently=False,
    )
