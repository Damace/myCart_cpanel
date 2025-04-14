from rest_framework import serializers
from .models import AdvertisementCategory
from .models import Advertisement

class AdvertisementCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementCategory
        fields = ['id', 'name', 'description', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']




class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'  # This will include all fields from the Advertisement model
