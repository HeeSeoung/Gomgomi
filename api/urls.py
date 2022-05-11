from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ChatbotView, QuotesViewSet

router = DefaultRouter()
router.register('quotes', QuotesViewSet, basename='quotes')

app_name = 'api'

urlpatterns = [
    path('chatbot/', ChatbotView.as_view(), name='chatbot'),
    path('', include(router.urls)),
]
