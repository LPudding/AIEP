# Generated by Django 2.1.3 on 2020-01-15 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('privileges', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
    ]
