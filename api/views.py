import json

import requests
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import chat_info, life_quotes
from .serializers import ChatbotSerializer, QuotesSerializer


class QuotesViewSet(viewsets.ModelViewSet):
    queryset = life_quotes.objects.all()
    serializer_class = QuotesSerializer

    def get_queryset(self):
        return life_quotes.objects.order_by("?").first()

    def list(self, request):
        queryset = self.get_queryset()
        serializers = QuotesSerializer(queryset)
        return Response(serializers.data)


class ChatbotView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )

    def get(self, request):

        user = request.user.id
        queryset = chat_info.objects.filter(user=user)
        serializers = ChatbotSerializer(queryset, many=True)

        return Response(serializers.data)

    def post(self, request):
        context = {}
        sent = request.data['sent']
        create_chatinfo(
            user=request.user.id,
            context=sent,
            chat_flag=0
        )
        data = {'sent': sent}
        response = requests.post(
            'http://127.0.0.1:8000/predict', data=json.dumps(data))
        result = response.json()['response']
        create_chatinfo(
            user=request.user.id,
            context=result,
            chat_flag=1,
        )
        return Response(result)


def create_chatinfo(**kwargs):
    created = chat_info.objects.create(
        user=kwargs.get('user', None),
        context=kwargs.get('context', None),
        chat_flag=kwargs.get('chat_flag', None)
    )
    return created
