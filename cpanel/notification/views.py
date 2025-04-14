from rest_framework import generics
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListCreateView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()  # Retrieve all notifications
    serializer_class = NotificationSerializer  # Use the NotificationSerializer to convert data



class NotificationDestroyView(generics.DestroyAPIView):
    queryset = Notification.objects.all()  # Define the queryset
    serializer_class = NotificationSerializer  # Use the NotificationSerializer for the response
    lookup_field = 'pk'  # URL should use 'pk' to specify the notification to delete


# # notifications/views.py
# import firebase_admin
# from firebase_admin import credentials, messaging
# from django.conf import settings
# from django.http import JsonResponse

# # Initialize Firebase Admin SDK
# cred = credentials.Certificate(settings.FIREBASE_SERVICE_ACCOUNT)
# firebase_admin.initialize_app(cred)

# def send_push_notification(token, title, body, image_url, data=None):
#     message = messaging.Message(
#         notification=messaging.Notification(
#             title=title,
#             body=body,
#             image=image_url,
#         ),
#         data=data or {},
#         token=token,
#     )
#     response = messaging.send(message)
#     return response

# def notify_user(request):
#     device_token = "e9ae6L_5QWu9WdtopT8WN8:APA91bFuUq6dulPQZSJkxMScJ2HyJXcxXSed3ur1NvUhl6PnTRbxySFBvE6_aTe1Y6BxC3HuynYFieyHYB_Xgz-J5GqQ8j4nPV5eeviNzUGj485NZOzOmF0"
#     image_url = "https://example.com/path/to/image.jpg"

#     response = send_push_notification(
#         token=device_token,
#         title="Hello, User!",
#         body="This is a test notification from Firebase.",
#         image_url=image_url,
#         data={"key1": "value1", "key2": "value2"}
#     )

#     return JsonResponse({"success": True, "response": str(response)})



#http://127.0.0.1:8000/notifications/notify/