# Generated by Django 4.2.7 on 2024-03-07 10:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_bio_user_following_user_gender_user_phone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="following",
            field=models.ManyToManyField(
                blank=True, related_name="followers", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]