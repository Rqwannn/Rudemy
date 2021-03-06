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
    path('auth/', views.LoginAuthentication, name='LoginAuth'),
    path('profileUser/<str:user>', views.getSingleUser, name='ProfileUser'),
    path('getUser/<str:pk>', views.UserProfile, name='GetUser'),
    path('editUser/', views.EditUser, name='EditUser'),
    path('UpdateProfileImg/', views.UpdateProfileImg, name='UpdateProfileImg'),
    path('UpdateStatusProfile/', views.UpdateStatusProfile,
         name='UpdateStatusProfile'),
    path('getCourse/<str:pk>', views.UserCourse, name='GetCourse'),
    path('insertCourse/', views.InsertCourse, name='InsertCourse'),
    path('deleteCourse/<str:pk>', views.DeleteCourse, name='DeleteCourse'),
    path('deleteCourseTag/<str:TagID>/<str:CourseID>',
         views.DeleteCourseTag, name='DeleteTagCourse'),
    path('editCourse/', views.EditCourse, name='EditCourse'),
    path('course/', views.CourseAPI.as_view(), name='Course'),
    path('insertReview/', views.ReviewCourse, name='insertReview'),
    path('getMessage/<str:pk>', views.getMessage, name='Inbox'),
    path('UserMassage/<str:pk>', views.userMessage, name='UserMassage'),
    path('InsertMessage/', views.InsertMessage, name='InsertMassage'),
    path('InsertSkill/', views.InsertSkill, name='InsertSkill'),
    path('DeleteSkill/<str:pk>', views.DeleteSkill, name='DeleteSkill'),
]
