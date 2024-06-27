from django.db import models
from customer.models import Customer


class NotifyEvent(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_email = models.BooleanField(default=True)
    is_sms = models.BooleanField(default=True)
    is_push = models.BooleanField(default=True)
    always_send = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]


class Notification(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    event = models.ForeignKey(
        NotifyEvent,
        on_delete=models.CASCADE,
        related_name="notifications",
        null=True,
        blank=True,
    )
    timestamp = models.DateTimeField()
    isRead = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer}"

    class Meta:
        ordering = ["-timestamp"]
