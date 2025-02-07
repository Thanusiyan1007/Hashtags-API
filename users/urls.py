from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RequestPasswordResetView, PasswordResetConfirmView, RegisterUserView, VerifyEmailView,LogoutView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('verify-email/<uidb64>/<token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('password-reset/', RequestPasswordResetView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
