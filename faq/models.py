# models.py

from django.db import models


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    helpful_count = models.PositiveIntegerField(default=0)
    not_helpful_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ["id"]

    def mark_as_helpful(self):
        self.helpful_count += 1
        self.save()

    def mark_as_not_helpful(self):
        self.not_helpful_count += 1
        self.save()
