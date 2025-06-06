from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AppUpdate

@admin.register(AppUpdate)
class AppUpdateAdmin(admin.ModelAdmin):
    list_display = ('version', 'status', 'updated_at')
