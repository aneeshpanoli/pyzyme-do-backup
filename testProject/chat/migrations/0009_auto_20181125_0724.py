# Generated by Django 2.1.2 on 2018-11-25 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_auto_20181125_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='username',
            name='uid',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
