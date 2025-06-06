from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AppUpdate

@api_view(['GET'])
def check_app_update(request):
    latest_update = AppUpdate.objects.last()
    if latest_update:
        return Response({
            'status': latest_update.status,
            'version': latest_update.version,
            'message': latest_update.message,
            'download_url': latest_update.download_url,
        })
    return Response({'status': 'not_available'})
