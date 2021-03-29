from django.urls import path

from .views import UserListView, UserApToAdmin, UpdateUserProfileView

urlpatterns = [
    path('', UserListView.as_view(), name='all_users'),
    path('/<int:pk>/to_admin', UserApToAdmin.as_view(), name='up_to_admin'),
    path('/<int:pk>/profile', UpdateUserProfileView.as_view(), name='update_profile')
]
