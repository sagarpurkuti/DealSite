# Generated by Django 5.0.3 on 2024-05-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='url',
            field=models.URLField(default='http://breadfruit.me'),
        ),
    ]
