# Generated by Django 5.0.1 on 2024-04-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_gamelist", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="initial_release",
            field=models.DateTimeField(null=True),
        ),
    ]
