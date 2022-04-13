from django.db import models

class chat_info(models.Model):
    '''
    - user and chatbot conversation data
    '''
    user = models.CharField(db_column='user', max_length=100, blank=True, null=True)
    context = models.CharField(db_column='context', max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    chat_flag = models.CharField(db_column='chat_flag', max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'chat_info'
        ordering = ['created']