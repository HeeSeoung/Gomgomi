from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ChatbotView, QuotesViewSet, VoiceChatbotView

router = DefaultRouter()
router.register('quotes', QuotesViewSet, basename='quotes')

app_name = 'api'

urlpatterns = [
    path('chatbot/', ChatbotView.as_view(), name='chatbot'),
    path('voice_chatbot/', VoiceChatbotView.as_view(), name='voice_chatbot'),
    path('', include(router.urls)),
]

