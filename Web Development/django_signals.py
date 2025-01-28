"""
Django’s Signals framework allows for decoupled components to communicate
with each other by sending notifications when certain events occur. Signals are especially
useful when certain actions need to trigger specific behavior in other parts of the application,
such as sending an email after user registration.
Django provides several built-in signals (e.g., post_save, pre_delete), and custom signals
can also be defined.
"""

# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from .emails import send_welcome_email

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        send_welcome_email(instance.email)
        print('Welcome email sent to', instance.email)