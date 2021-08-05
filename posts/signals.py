from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment
from .tasks import mail_new_comment, mail_accepted_comment


@receiver(post_save, sender=Comment)
def new_comment(instance, created, **kwargs):
    if created:
        mail_new_comment.delay(instance.id)
    else:
        if instance.accept:
            mail_accepted_comment.delay(instance.id)
