from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertisementViewSet,AdvertisementByCategoryView
from .views import OfferListCreateAPIView
from .views import AdvertisementCategoryAPIView, AdvertisementCategoryDetailAPIView
from .views import AdvertisementListCreateAPIView, AdvertisementRetrieveUpdateDestroyAPIView

router = DefaultRouter()
router.register(r'advertisements', AdvertisementViewSet)

urlpatterns = [
    path('advertisement-categories/', AdvertisementCategoryAPIView.as_view(), name='advertisement-category-list'),
    path('advertisement-categories/<int:pk>/', AdvertisementCategoryDetailAPIView.as_view(), name='advertisement-category-detail'),
    path('api/', include(router.urls)),  # Include the router URLs under the '/api/' path
    path('api/category/<int:category_id>/advertisements/', AdvertisementByCategoryView.as_view(), name='advertisements_by_category_api'),
    path('offers/', OfferListCreateAPIView.as_view(), name='offer-list-create'),
    path('advertisements/', AdvertisementListCreateAPIView.as_view(), name='advertisement-list-create'),
    path('advertisements/<int:pk>/', AdvertisementRetrieveUpdateDestroyAPIView.as_view(), name='advertisement-detail'),


]
