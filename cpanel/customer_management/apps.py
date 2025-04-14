from django.apps import AppConfig


class CustomerManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer_management'
    label = "customer_management"
    verbose_name = "customer and orders management"
