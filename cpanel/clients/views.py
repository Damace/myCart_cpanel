from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClientProfileSerializer
from rest_framework import generics
from .models import ClientProfile
from rest_framework.exceptions import NotFound
from django.http import JsonResponse


@api_view(['POST'])
def create_Client_profile(request):
    if request.method == 'POST':
        serializer = ClientProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def userprofile_update(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')

            # Check if a profile with the given email exists
            client_profile = ClientProfile.objects.filter(email=email).first()

            if client_profile:
                client_profile.address = data.get('address', client_profile.address)
                client_profile.postal_code = data.get('postal_code', client_profile.postal_code)
                client_profile.phone_number = data.get('phone_number', client_profile.phone_number)
                client_profile.password = data.get('password', client_profile.password)
                client_profile.agree_term_and_condition = data.get('agree_terms', client_profile.agree_term_and_condition)
                client_profile.save()

                return JsonResponse({'message': 'Profile updated successfully'}, status=200)
            else:
                return JsonResponse({'error': 'No profile found with this email'}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)








def register_google_user(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)

        profile = ClientProfile.create_from_google(data)
        return JsonResponse({"message": "User registered successfully", "user_id": profile.user.id}, status=201)

    return JsonResponse({"error": "Invalid request"}, status=400)



from rest_framework.views import APIView
from .serializers import GoogleSignInSerializer

class GoogleSignInView(APIView):
    def post(self, request):
        """
        Handles Google Sign-In user registration or login.
        """
        serializer = GoogleSignInSerializer(data=request.data)
        if serializer.is_valid():
            user, profile = serializer.create_or_update_user()
            return Response(
                {
                    "message": "User authenticated successfully",
                    "user_id": user.id,
                    "full_name": profile.full_name,
                    "email": profile.email,
                    "profile_picture": profile.profile_picture,
                    "country": profile.country,
                    "region": profile.region,
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def create_Client_profile(request):
    if request.method == 'POST':
        phone_number = request.data.get('phone_number')

        # Use filter().first() to check if a ClientProfile exists
        Client_profile = ClientProfile.objects.filter(phone_number=phone_number).first()

        if Client_profile is None:
            # If not found, create a new profile
            serializer = ClientProfileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)  # 201 for created
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # If found, update the existing profile
            serializer = ClientProfileSerializer(Client_profile, data=request.data, partial=True)  # Allow partial updates
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)  # 200 for update
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientProfileList(generics.ListAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer



class ClientProfileDetail(generics.RetrieveAPIView):
    serializer_class = ClientProfileSerializer

    def get_object(self):
        phone_number = self.kwargs.get('phone_number')
        try:
            return ClientProfile.objects.get(phone_number=phone_number)
        except ClientProfile.DoesNotExist:
            raise NotFound(detail="ClientProfile not found.")