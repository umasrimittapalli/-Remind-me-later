from django.db import models
from django.utils import timezone

# Create your models here.
class Reminder(models.Model):
    Reminder_choices=[
        ('sms','SMS'),
        ('email','Email'),
    ]
    message = models.TextField()
    date=models.DateField()
    time =models.TimeField()
    Reminder_method =models.CharField(max_length=10 ,choices=Reminder_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_sent = models.BooleanField(default=False)
    sent_at = models.DateTimeField(null=True, blank=True)
     
    class Meta:
        ordering = ['date', 'time']
        verbose_name = 'Reminder'
        verbose_name_plural = 'Reminders'

    def __str__(self):
        return f'Reminder: {self.message} on  {self.date} at {self.time}'
    
    def mark_as_sent(self):
        self.is_sent = True
        self.sent_at = timezone.now()
        self.save()

    @property
    def is_due(self):
        """Check if the reminder is due to be sent"""
        now = timezone.now()
        reminder_datetime = timezone.make_aware(
            timezone.datetime.combine(self.date, self.time)
        )
        return reminder_datetime <= now and not self.is_sent