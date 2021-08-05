from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Mailing
from .tasks import send_mailing


@receiver(post_save, sender=Mailing)
def new_comment(instance, created, **kwargs):
    if created:
        send_mailing.delay(instance.id)

