# Generated by Django 3.0.1 on 2020-01-09 13:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200109_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpictureinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c1f408ca-3a26-491b-b7ff-2543de35b035'), help_text='Уникальный идентификатор', primary_key=True, serialize=False),
        ),
    ]
