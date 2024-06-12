from django.db import models
from customer.models import Customer


class Notification(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField()
    isRead = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]
