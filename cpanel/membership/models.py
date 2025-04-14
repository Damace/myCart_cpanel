from django.db import models

class MembershipType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.PositiveIntegerField(help_text="Duration in months")

    def __str__(self):
        return self.name

class Member(models.Model):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    membership_type = models.ForeignKey('MembershipType', on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    # New fields
    name = models.CharField(max_length=100, null=True, blank=True)  # Membership name
    price = models.CharField(max_length=50, null=True, blank=True)  # Price as string
    duration = models.CharField(max_length=50, null=True, blank=True)  # Duration of membership
    benefits = models.TextField(null=True, blank=True)
    offer = models.TextField(null=True, blank=True)  # Offer details
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.phone_number} - {self.name or 'No Membership'}"
