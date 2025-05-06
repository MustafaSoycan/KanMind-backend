from django.urls import path
from .views import userProfileList, userProfileDetail, CustomLoginView, RegistrationView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('profiles/', userProfileList.as_view(), name='userprofile-list'),
    # path('profiles/<int:pk>/', userProfileDetail.as_view(),
    #      name='userprofile-detail'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
