from django.contrib import admin
from .models import ClientProfile


@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone_number', 'email', 'postal_code', 'address','password')
    search_fields = ('full_name','phone_number')
    list_filter = ('full_name','phone_number')
    ordering = ('full_name',)


   
  
