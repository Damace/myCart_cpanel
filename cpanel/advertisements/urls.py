from django.urls import path
from .views import AdvertisementCategoryAPIView, AdvertisementCategoryDetailAPIView

urlpatterns = [
    path('advertisement-categories/', AdvertisementCategoryAPIView.as_view(), name='advertisement-category-list'),
    path('advertisement-categories/<int:pk>/', AdvertisementCategoryDetailAPIView.as_view(), name='advertisement-category-detail'),

]


# advertisements/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertisementViewSet,AdvertisementByCategoryView

# Create a router and register the AdvertisementViewSet with it
router = DefaultRouter()
router.register(r'advertisements', AdvertisementViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Include the router URLs under the '/api/' path
    path('api/category/<int:category_id>/advertisements/', AdvertisementByCategoryView.as_view(), name='advertisements_by_category_api'),

]

from .views import OfferListCreateAPIView

urlpatterns = [
    path('offers/', OfferListCreateAPIView.as_view(), name='offer-list-create'),
]



