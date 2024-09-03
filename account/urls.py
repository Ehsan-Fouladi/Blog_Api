from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/register/', views.RegisterUserApiView.as_view()),
    path('api/change_password/', views.ChangePasswordApiView.as_view(), name='change_password'),
    path('api/profile/', views.ProfileUserApiView.as_view()),
    path('api/profile/update/', views.ProfileUserUpdateApiView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]