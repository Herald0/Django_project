# Generated by Django 5.0.2 on 2024-05-21 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_like_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislike_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
