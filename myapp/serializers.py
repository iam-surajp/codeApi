from rest_framework import serializers
from .models import Company, Client,ClientUsers
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            message='Enter a valid email address',
        ),
    ])

    class Meta:
        model = User
        fields = '__all__'

# Define other serializers with regex validation as required


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientUsers
        fields = '__all__'