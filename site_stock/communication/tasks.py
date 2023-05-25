from better_profanity import profanity
from celery import shared_task

from .models import Message

profanity.load_censor_words()

@shared_task()
def replace_text_with_censored(comment_id):
    """ A function that detects bad words in comments and mute them """

    comment = Message.objects.get(id=comment_id)
    censored_text = profanity.censor(comment.content)
    comment.content = censored_text
    comment.save()
