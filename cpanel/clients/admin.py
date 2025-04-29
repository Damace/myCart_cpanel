from django.contrib import admin


@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone_number', 'email', 'postal_code', 'address', 'region', ' password')
    search_fields = ('full_name','phone_number')
    list_filter = ('full_name','phone_number')
    ordering = ('full_name',)


   
  
