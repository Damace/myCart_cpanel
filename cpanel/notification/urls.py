from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.NotificationListCreateView.as_view(), name='notification_list_create'),  # For GET and POST requests
    path('notifications/<int:pk>/', views.NotificationDestroyView.as_view(), name='notification_delete'),  # For DELETE requests
]
