from rest_framework import serializers
from auth_app.models import UserProfile
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'location']


class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)
    fullname = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ['fullname', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self, **kwargs):
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']
        if pw != repeated_pw:
            raise serializers.ValidationError("Passwords do not match")

        email = self.validated_data['email']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        account = User(
            email=self.validated_data['email'], username=self.validated_data['fullname'])
        account.set_password(pw)
        account.save()
        return account
