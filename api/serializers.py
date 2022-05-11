from django.contrib.auth.models import User
from rest_framework import serializers

from .models import chat_info, life_quotes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class ChatbotSerializer(serializers.ModelSerializer):
    class meta:
        model = chat_info
        fields = '__all__'


class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = life_quotes
        fields = '__all__'
