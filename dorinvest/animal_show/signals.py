from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import EndedShow

@receiver(m2m_changed, sender=EndedShow.photoreport.through)
def clear_photoreport(sender, instance, action, **kwargs):
    if action == "post_add":
        instance.photoreport.clear()