from rest_framework import serializers
from review_management.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'rating', 'comment', 'created', 'updated']
