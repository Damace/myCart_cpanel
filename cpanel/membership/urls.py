from django.urls import path
from .views import MemberAPI, MemberByPhoneAPI,DellMemberByPhoneAPI,UpsertMemberAPI

urlpatterns = [
    path('members/upsert/', UpsertMemberAPI.as_view(), name='upsert_member'),
    path('members/', MemberAPI.as_view(), name='member_api'),  # Existing endpoint
    path('members/<str:phone_number>/', MemberByPhoneAPI.as_view(), name='member_by_phone_api'),  # New endpoint
    path('del_members/<str:phone_number>/', DellMemberByPhoneAPI.as_view(), name='member_by_phone_api'),
]