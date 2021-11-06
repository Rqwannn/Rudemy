from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterUser, name='Register'),
    path('profile/', views.ProfileAPI.as_view(), name='Profile'),
    path('course/', views.CourseAPI.as_view(), name='Course'),
    path('auth/', views.LoginAuthentication, name='LoginAuth'),
    path('profileUser/<str:user>', views.getSingleUser, name='ProfileUser'),
]
