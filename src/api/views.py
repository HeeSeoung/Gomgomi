import base64
import io
import json
import os
from io import StringIO
from django.http import FileResponse

import requests
from django.core.files.base import ContentFile
from django.utils.crypto import get_random_string
from google.cloud import speech
from pydub import AudioSegment
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import UserSentiment

from .models import chat_info, life_quotes, voice_chat_info
from .serializers import (
    ChatbotSerializer,
    QuotesSerializer,
    SentimentSerializer,
    VoiceChatbotSerializer,
)

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"
] = "/home/gnltmd23/google/vivid-spot-352208-f7e0462f8e6d.json"


class QuotesViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
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
    authentication_classes = (TokenAuthentication,)

    def get(self, request):

        user = request.user.id
        queryset = chat_info.objects.filter(user=user)
        serializers = ChatbotSerializer(queryset, many=True)

        return Response(serializers.data)

    def post(self, request):
        context = {}
        sent = request.data["sent"]
        create_chatinfo(user=request.user.id, context=sent, chat_flag=0)
        data = {"sent": sent}
        response = requests.post(
            "http://34.64.69.248:8000/predict", data=json.dumps(data)
        )
        result = response.json()["response"]
        create_chatinfo(
            user=request.user.id, context=result, chat_flag=1,
        )
        return Response(result)


class VoiceChatbotView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get(self, request):

        user = request.user.id
        queryset = chat_info.objects.filter(user=user)
        serializers = ChatbotSerializer(queryset, many=True)

        return Response(serializers.data)

    def post(self, request):
        context = {}
        try:
            voice = request.FILES["voice"]
        except Exception as e:
            print(e)
            voice = request.POST["voice"]
            voice = base64.b64decode(voice)

        # instantiates a client
        client = speech.SpeechClient()
        audio = speech.RecognitionAudio(content=voice)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=48000,
            audio_channel_count=2,
            language_code="ko-KR",
        )

        # detects speech in the audio file
        response = client.recognize(config=config, audio=audio)
        text = response.results[0].alternatives[0].transcript

        # create user voice data
        create_voice_chatinfo(
            user=request.user.id, context=text, chat_flag=0
        )

        # request chatbot api
        data = {"sent": text}
        response = requests.post(
            "http://34.64.69.248:8000/predict", data=json.dumps(data)
        )
        result = response.json()["response"]

        # kakao api : TTS
        headers = {
            "Authorization": f"KakaoAK 80b269050cd58c9743d68720ddc84692",
            "Content-Type": "application/xml",
        }
        data = f'<voice name="WOMAN_DIALOG_BRIGHT">{result}</voice>'
        response = requests.post(
            "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize",
            headers=headers,
            data=data.encode(encoding="utf-8"),
        )
        create_voice_chatinfo(
            user=request.user.id,
            context=result,
            chat_flag=1,
            voice=ContentFile(response.content),
        )

        context["response"] = result
        # context["voice"] = io.BytesIO(response.content)

        return Response(context)


class SentimentView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        user = request.user.id
        queryset = UserSentiment.objects.filter(user=user)
        serializers = SentimentSerializer(queryset, many=True)

        return Response(serializers.data)


def create_chatinfo(**kwargs):
    created = chat_info.objects.create(
        user=kwargs.get("user", None),
        context=kwargs.get("context", None),
        chat_flag=kwargs.get("chat_flag", None),
    )
    return created


def create_voice_chatinfo(**kwargs):
    created = voice_chat_info.objects.create(
        user=kwargs.get("user", None),
        context=kwargs.get("context", None),
        voice=kwargs.get("voice", None),
        chat_flag=kwargs.get("chat_flag", None),
    )
    return created
