from django.db import models

class AdvertisementCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Name of the advertisement category (e.g., 'Flash Sales').")
    description = models.TextField(blank=True, null=True, help_text="Optional description of the advertisement category.")
    is_active = models.BooleanField(default=True, help_text="Indicates whether this category is currently active.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Advertisement Category"
        verbose_name_plural = "Advertisement Categories"
        ordering = ['name']

    def __str__(self):
        return self.name
        

class Advertisement(models.Model):
    category = models.ForeignKey(AdvertisementCategory, on_delete=models.CASCADE, related_name="advertisements")
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='advertisements/images/')
    link = models.URLField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.category.name}"

