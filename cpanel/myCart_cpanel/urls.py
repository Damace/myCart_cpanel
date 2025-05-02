# """
# URL configuration for myCart_cpanel project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))   


# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


# """


# from django.contrib import admin
# from django.urls import path, include

# from django.conf import settings
# from django.conf.urls.static import static
# from product_management.views import ProductListCreateView, ProductRetrieveUpdateDeleteView


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('product_management.urls')), 
#     path('api/', include('review_management.urls')), 
#     path('api/', include('review_management.urls')),
#     # path('notifications/', include('notifications.urls')),
    
    
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
# from .views import ProductReviewViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('product_management.urls')),
    path('', include('clients.urls')),
    path('', include('orders.urls')),
    path('', include('membership.urls')),
    path('', include('advertisements.urls')),
    path('api/', include('advertisements.urls')),
    path('advertisements/', include('advertisements.urls')),
    path('', include('clients.urls')),
    path('api/', include('review_management.urls')),
    # path('api/', include('offers.urls')),
    # path('notification/', include('notification.urls')),
    # path('api_reviews/', include(router.urls)),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
