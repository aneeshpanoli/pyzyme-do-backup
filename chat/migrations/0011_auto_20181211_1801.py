# Generated by Django 2.1.2 on 2018-12-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_message_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='stars',
            field=models.CharField(default='0|0|0', max_length=500),
        ),
    ]
