from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

import requests

# Create your views here.
class ChatbotView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )

    def get(self, request):
        context = {}
        user = request.user.id
        sent = request.data['sent']

        data = {'sent': sent }
        response = requests.post('http://127.0.0.1:8000/predict', data=data)
        print(response)

        return Response(context)