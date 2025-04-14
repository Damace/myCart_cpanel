from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDeleteView
from .views import update_product
from .views import ProductReviewCreateView


urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),  # List and create products
    path('products/<int:pk>/', ProductRetrieveUpdateDeleteView.as_view(), name='product-detail'),  # Retrieve, update, delete products by ID
    path('update-product/', update_product, name='update-product'),
    path('reviews/', ProductReviewCreateView.as_view(), name='review-create'),
]


