from django.db import models

class AppUpdate(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    ]
    version = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    message = models.TextField(blank=True, null=True)
    download_url = models.URLField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Delete all existing records before saving the new one
        AppUpdate.objects.all().delete()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Version {self.version} - {self.status}"
