from django.urls import path
from .views import check_app_update

urlpatterns = [
    path('check/', check_app_update, name='check_app_update'),
]
