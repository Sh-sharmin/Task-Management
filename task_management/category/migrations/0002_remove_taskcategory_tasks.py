# Generated by Django 5.0.7 on 2024-12-23 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskcategory',
            name='tasks',
        ),
    ]
