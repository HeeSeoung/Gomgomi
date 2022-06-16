# Generated by Django 3.2.7 on 2022-04-15 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat_info',
            options={'ordering': ['created']},
        ),
        migrations.RemoveField(
            model_name='chat_info',
            name='created_at',
        ),
        migrations.AddField(
            model_name='chat_info',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]