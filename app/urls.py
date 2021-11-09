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
    path('getMessage/<str:pk>', views.getMessage, name='Inbox'),
    path('getUser/<str:pk>', views.UserProfile, name='GetUser'),
    path('getCourse/<str:pk>', views.UserCourse, name='GetCourse'),
    path('insertReview/', views.ReviewCourse, name='insertReview'),
]
