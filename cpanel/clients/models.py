from django.db import models
from django.contrib.auth.hashers import make_password


class ClientProfile(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    postal_code = models.CharField(max_length=10)
    address = models.TextField()
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        # Encrypt the password before saving
        if not self.pk:  # Only hash when creating, not when updating
            self.password = make_password(self.password)
        super(ClientProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name




