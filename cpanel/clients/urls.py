from django.urls import path
from .views import create_Client_profile
from .views import ClientProfileList,ClientProfileDetail
from .views import GoogleSignInView
from .views import RegisterCustomerView, LoginCustomerView
from . import views  # Assuming your views are in the same directory


urlpatterns = [
    path('api/userprofile/', create_Client_profile, name='create_Client_profile'),
    path('api/clientsprofiles/', ClientProfileList.as_view(), name='client_profile_list'),
    path('api/clientprofile/<str:phone_number>/', ClientProfileDetail.as_view(), name='client_profile_detail'),
    path('google-signin/', GoogleSignInView.as_view(), name='google-signin'),
    path('userprofile_update/', views.userprofile_update, name='userprofile_update'),
    path('api/register/', RegisterCustomerView.as_view(), name='register'),
    path('api/login/', LoginCustomerView.as_view(), name='login'),
]

