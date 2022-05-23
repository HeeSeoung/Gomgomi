from django.db import models


class chat_info(models.Model):
    """
    - user and chatbot conversation data
    """

    user = models.CharField(max_length=100, blank=True, null=True)
    context = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    chat_flag = models.CharField(max_length=10, blank=True, null=True)
    conversation_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "chat_info"
        ordering = ["created"]


class voice_chat_info(models.Model):
    """
    - user and chatbot voice conversation data
    """

    user = models.CharField(max_length=100, blank=True, null=True)
    context = models.CharField(max_length=200, blank=True, null=True)
    voice = models.FileField(upload_to="voice_chat/")
    created = models.DateTimeField(auto_now_add=True, null=True)
    chat_flag = models.CharField(max_length=10, blank=True, null=True)
    conversation_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "voice_chat_info"
        ordering = ["created"]


class life_quotes(models.Model):
    """
    - life quotes data
    """

    sentence = models.TextField(db_column="sentence")
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "life_quotes"
        ordering = ["created"]
