from django.urls import path
from .views import ReviewListCreateView, SubmitReviewView, ProductReviewListAPIView

urlpatterns = [
    path('products/<int:product_id>/reviews/', ReviewListCreateView.as_view(), name='product-reviews'),
    path('submit-review/', SubmitReviewView.as_view(), name='submit-review'),
    path('product/<int:product_id>/reviews/', ProductReviewListAPIView.as_view(), name='product-reviews'),
]

