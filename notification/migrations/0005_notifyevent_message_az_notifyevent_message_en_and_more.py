# Generated by Django 5.0.6 on 2024-06-26 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notification", "0004_notifyevent_alter_notification_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="notifyevent",
            name="message_az",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="notifyevent",
            name="message_en",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="notifyevent",
            name="message_ru",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="notifyevent",
            name="title_az",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="notifyevent",
            name="title_en",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="notifyevent",
            name="title_ru",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]