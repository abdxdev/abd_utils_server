# Generated by Django 5.1 on 2024-09-05 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="settings",
            name="token_pickle_base64",
        ),
    ]
