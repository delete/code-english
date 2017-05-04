from django.db import models

from backend.user.models import User


class Message(models.Model):

    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='messages_sender'
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='messages_receiver'
    )

    subject = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
