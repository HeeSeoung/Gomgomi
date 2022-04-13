from django.urls import path, include
from .views import ChatbotView
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

app_name = 'api'

urlpatterns = [
    path('chatbot/', ChatbotView.as_view(), name='chatbot'),
]

