# Generated by Django 2.1.2 on 2018-12-11 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_auto_20181211_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='stars',
        ),
    ]