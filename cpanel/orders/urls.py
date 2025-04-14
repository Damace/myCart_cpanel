from django.urls import path
from orders.views import ClientProfileListCreateAPIView,OrderListCreateAPIView, OrderItemListCreateAPIView, PaymentListCreateAPIView
from .views import ProductOrdersAPIView
from .views import ProductOrdersView
# from .views import ProductOrdersByPhoneView
from .views import OrdersByPhoneAndStatusAPIView
from .views import create_review
from .views import get_reviews_by_product




urlpatterns = [
    path('client-profiles/', ClientProfileListCreateAPIView.as_view(), name='client-profile-list-create'),
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('order-items/', OrderItemListCreateAPIView.as_view(), name='order-item-list-create'),
    path('payments/', PaymentListCreateAPIView.as_view(), name='payment-list-create'),
    path('product-orders/', ProductOrdersAPIView.as_view(), name='product-orders-api'),
        # Retrieve all orders or a specific order by ID
    path('orders/', ProductOrdersView.as_view(), name='orders_list'),
    path('orders/<int:id>/', ProductOrdersView.as_view(), name='order_detail'),
        # Retrieve orders by phone number
    # path('orderss/phone/<str:phone_number>/', ProductOrdersByPhoneView.as_view(), name='orders_by_phone'),
    path('orders/phone/<str:phone_number>/', OrdersByPhoneAndStatusAPIView.as_view(), name='orders_by_phone_and_status'),
    path('submit-review/', create_review, name='submit-review'),
    path('reviews/<int:product_id>/', get_reviews_by_product, name='get_reviews_by_product'),

]

