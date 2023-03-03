from rest_framework import serializers
from apps.users.models import User
import django.contrib.auth.password_validation as validators
from django.core import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.profiles.models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2',]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match"})
        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=attrs['password'])
            # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return attrs
    
    def create(self, validated_data):
        if User.objects.filter(email=validated_data["email"]).exists():
            raise serializers.ValidationError({"email": "Email already exists"})
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        user.save()
        profile = Profile.objects.create(user=user)
        profile.save()

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        profile = Profile.objects.get(user=self.user)
        data.update({
                        'user':
                            {
                                'id': self.user.id,
                                'email': self.user.email,
                                'is_superuser': self.user.is_superuser
                            },
                        'profile':
                            {
                                'id': profile.id,
                                'first_name': profile.first_name,
                                'last_name': profile.last_name,
                                'phone': profile.phone
                            }
                     })
        # and everything else you want to send in the response
        return data


class CustomJWTSerializer(MyTokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {
            'email': '',
            'password': attrs.get("password")
        }
        # This is answering the original question, but do whatever you need here.
        # For example in my case I had to check a different model that stores more user info
        # But in the end, you should obtain the username to continue.
        user_obj = User.objects.filter(email=attrs.get("email")).first()
        if user_obj:
            credentials['email'] = user_obj.email

        return super().validate(credentials)