# views.py
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
# views.py
from rest_framework import viewsets
from .models import ProductReview
from .serializers import ProductReviewSerializer

# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@csrf_exempt
def update_product(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            product_name = data.get('product_name')  # The product name sent from Flutter
            customer = data.get('customer')         # Customer data
            comments = data.get('comments')         # Comments
            comments_date = data.get('comments_date')  # Comments date

            # Fetch the product by name
            product = get_object_or_404(Product, name=product_name)

            # Update fields
            product.customer = customer
            product.comments = comments
            product.comments_date = comments_date
            product.save()

            return JsonResponse({'success': True, 'message': 'Product updated successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})


class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer



class ProductReviewListCreateView(APIView):
    """
    List all reviews or create a new review.
    """
    def get(self, request):
        reviews = ProductReview.objects.all()
        serializer = ProductReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new review to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ProductReviewCreateView(APIView):
    """
    Create a new product review.
    """
    def post(self, request):
        # Deserialize the incoming data
        serializer = ProductReviewSerializer(data=request.data)

        # Check if the data is valid
        if serializer.is_valid():
            # Save the new review to the database
            serializer.save()
            # Return the created review data with a success response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If the data is invalid, return an error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

