from django.db import models

class ClientProfile(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    google_uid = models.CharField(max_length=255, unique=True, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)  # Storing Google profile picture URL
    country = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)  # Added region field
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    agree_term_and_condition = models.BooleanField(default=False)  # Updated to BooleanField


    def __str__(self):
        return f"{self.full_name} - {self.country}"


