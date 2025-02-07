from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings

def generate_verification_token(user):
    """ Generate a unique email verification token """
    return default_token_generator.make_token(user)

def send_verification_email(user):
    """ Send verification email to user """
    token = generate_verification_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verification_link = f"{settings.FRONTEND_URL}/verify-email/{uid}/{token}/"

    email_subject = "Verify Your Email"
    email_body = f"Hello {user.username},\n\nPlease verify your email by clicking the link below:\n{verification_link}\n\nThank you!"

    send_mail(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False
    )
