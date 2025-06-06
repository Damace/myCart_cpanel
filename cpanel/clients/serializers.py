from rest_framework import serializers
from .models import ClientProfile

class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = '__all__'  # This will include all fields in the model



from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ClientProfile

User = get_user_model()

class GoogleSignInSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    google_uid = serializers.CharField(max_length=255)
    profile_picture = serializers.URLField(required=False, allow_blank=True)
    country = serializers.CharField(max_length=100, required=False, allow_blank=True)
    region = serializers.CharField(max_length=100, required=False, allow_blank=True)

    def create_or_update_user(self):
        """
        Creates or updates a user from Google Sign-In details.
        """
        data = self.validated_data

        # Create or update the User
        user, _ = User.objects.update_or_create(
            email=data["email"],
            defaults={
                "full_name": data["full_name"],
            }
        )

        # Create or update the ClientProfile
        profile, _ = ClientProfile.objects.update_or_create(
            user=user,
            defaults={
                "full_name": data["full_name"],
                "email": data["email"],
                "google_uid": data["google_uid"],
                "profile_picture": data.get("profile_picture", ""),
                "country": data.get("country", ""),
                "region": data.get("region", ""),
            },
        )

        return user, profile

from rest_framework import serializers
from .models import ClientProfile

class CustomerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile

        fields = ['full_name', 'phone_number', 'email', 'postal_code', 'address', 'password']

    def create(self, validated_data):
        return ClientProfile.objects.create(**validated_data)



class CustomerLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
