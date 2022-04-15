from rest_framework import serializers
from .models import chat_info
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class ChatbotSerializer(serializers.ModelSerializer):
    class meta:
        model = chat_info
        fields = '__all__'