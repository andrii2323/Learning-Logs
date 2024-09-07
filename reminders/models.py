from django.db import models
from django.contrib.auth.models import User
from learning_logs.models import Topic, Category


class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    reminder_date = models.DateTimeField()
    message = models.CharField(max_length=255)

    def __str__(self):
        return f'Reminder for {self.user} on {self.reminder_date}'
    
