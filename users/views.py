from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import RegisterUserSerializer
from .utils import send_verification_email
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegisterUserView(APIView):
    def post(self, request):
        """ Register user and send email verification """
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_verification_email(user)
            return Response({"message": "Registration successful. Check your email to verify your account."}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyEmailView(APIView):
    def get(self, request, uidb64, token):
        """ Verify user email and activate account """
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_object_or_404(User, pk=uid)
        except (TypeError, ValueError, OverflowError):
            return Response({"error": "Invalid verification link"}, status=status.HTTP_400_BAD_REQUEST)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({"message": "Email verified successfully. You can now log in."}, status=status.HTTP_200_OK)
        
        return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)

class RequestPasswordResetView(APIView):
    def post(self, request):
        """ Sends password reset email """
        email = request.data.get("email")
        user = User.objects.filter(email=email).first()

        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        reset_link = f"{settings.FRONTEND_URL}/password-reset-confirm/{uid}/{token}/"

        send_mail(
            "Password Reset Request",
            f"Click the link to reset your password: {reset_link}",
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

        return Response({"message": "Password reset email sent"}, status=status.HTTP_200_OK)

class PasswordResetConfirmView(APIView):
    def post(self, request, uidb64, token):
        """ Resets the password if the token is valid """
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_object_or_404(User, pk=uid)
        except (TypeError, ValueError, OverflowError):
            return Response({"error": "Invalid reset link"}, status=status.HTTP_400_BAD_REQUEST)

        if not default_token_generator.check_token(user, token):
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)

        new_password = request.data.get("password")
        user.set_password(new_password)
        user.save()

        return Response({"message": "Password reset successful"}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Requires authentication

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()  # ✅ Blacklist the refresh token

            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)