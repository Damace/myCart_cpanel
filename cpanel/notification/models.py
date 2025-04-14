from django.db import models

class Notification(models.Model):
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('normal', 'Normal'),
        ('low', 'Low'),
    ]
    
    title = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.URLField(blank=True, null=True, help_text="URL to the notification icon")
    action_url = models.URLField(blank=True, null=True, help_text="URL to redirect on notification click")
    is_read = models.BooleanField(blank=True, default=False)
    priority = models.CharField(blank=True, max_length=10, choices=PRIORITY_CHOICES, default='normal')
    time_to_live = models.PositiveIntegerField(blank=True, default=3600, help_text="Time in seconds for notification to live")
    created_at = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
