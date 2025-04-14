from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        product_id = self.kwargs['product_id']  # Get product_id from the URL
        return Review.objects.filter(product__id=product_id)  # Filter reviews by product_id

    def create(self, request, *args, **kwargs):
        product_id = self.kwargs['product_id']  # Get product_id from the URL
        request.data['product'] = product_id  # Assign product ID to the request data
        return super().create(request, *args, **kwargs)
    
#############################################################################################################
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from review_management.models import Review
from review_management.serializers import ReviewSerializer

class SubmitReviewView(APIView):
    """
    API View to handle review submission for a given product.
    """
    permission_classes = [IsAuthenticated]  # Require authentication to submit a review

    def post(self, request, *args, **kwargs):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Review submitted successfully!', 'review': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
