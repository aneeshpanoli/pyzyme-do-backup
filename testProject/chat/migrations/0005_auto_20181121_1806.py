# Generated by Django 2.1.2 on 2018-11-21 18:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='username',
            name='uid',
            field=models.CharField(default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]
