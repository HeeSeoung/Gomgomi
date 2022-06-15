from django.contrib.auth.models import User
from django.db import models


class UserSentiment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sentiment"
    )
    sentiment = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        db_table = "user_sentiment"
