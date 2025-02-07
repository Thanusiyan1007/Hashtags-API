from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

User = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']

    def validate_email(self, value):
        """ Check if email is valid and unique """
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid email format.")
        
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value

    def validate_username(self, value):
        """ Ensure username is unique """
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already taken.")
        return value

    def create(self, validated_data):
        """ Create user but set is_active=False until email is verified """
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        user.is_active = False  
        user.save()
        return user
