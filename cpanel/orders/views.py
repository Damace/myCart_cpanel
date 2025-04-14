from rest_framework import generics
from clients.models import  ClientProfile
from orders.models import Order,OrderItem,Payment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductOrdersSerializer
from .models import ProductOrders
from rest_framework.views import APIView



from .serializers import (
    ClientProfileSerializer,
    OrderSerializer, OrderItemSerializer, PaymentSerializer
)

class ClientProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class PaymentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer



class ProductOrdersAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ProductOrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Product order saved successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductOrdersView(APIView):
    def get(self, request, *args, **kwargs):
        """
        Retrieve all ProductOrders or a specific one by ID.
        """
        order_id = kwargs.get('id')
        if order_id:
            try:
                order = ProductOrders.objects.get(id=order_id)
                serializer = ProductOrdersSerializer(order)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except ProductOrders.DoesNotExist:
                return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            orders = ProductOrders.objects.all()
            serializer = ProductOrdersSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create a new ProductOrder.
        """
        serializer = ProductOrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        Delete a ProductOrder by ID.
        """
        order_id = kwargs.get('id')
        try:
            order = ProductOrders.objects.get(id=order_id)
            order.delete()
            return Response({'message': 'Order deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except ProductOrders.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)




class ProductOrdersByPhoneView(APIView):
    def get(self, request, phone_number, *args, **kwargs):
        """
        Retrieve ProductOrders by phone number.
        """
        orders = ProductOrders.objects.filter(phone_number=phone_number)
        if orders.exists():
            serializer = ProductOrdersSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No orders found for this phone number'}, status=status.HTTP_404_NOT_FOUND)




class OrdersByPhoneAndStatusAPIView(APIView):
    def get(self, request, phone_number, *args, **kwargs):
        # Retrieve query parameters for `order_status`
        order_status = request.query_params.get('order_status', None)

        # Filter orders by phone number and optionally by order_status
        if order_status:
            orders = ProductOrders.objects.filter(phone_number=phone_number, order_status=order_status)
        else:
            orders = ProductOrders.objects.filter(phone_number=phone_number)

        if not orders.exists():
            return Response(
                {"detail": "No orders found for this phone number or status."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ProductOrdersSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



from rest_framework.decorators import api_view
from .serializers import ItemReviewSerializer

@api_view(['POST'])
def create_review(request):
    serializer = ItemReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Review submitted successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import api_view
from .models import ItemReview

@api_view(['GET'])
def get_reviews_by_product(request, product_id):
    reviews = ItemReview.objects.filter(product_id=product_id)  # Filter reviews by product_id
    serializer = ItemReviewSerializer(reviews, many=True)  # Serialize multiple objects
    return Response(serializer.data)  # Return JSON response




