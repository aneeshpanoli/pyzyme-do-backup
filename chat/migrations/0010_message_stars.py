# Generated by Django 2.1.2 on 2018-12-11 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_auto_20181125_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='stars',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]