# Generated by Django 3.2.8 on 2022-01-06 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_input_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='user',
        ),
        migrations.DeleteModel(
            name='TUMOR_IMAGE',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
