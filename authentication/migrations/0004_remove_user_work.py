# Generated by Django 3.2.16 on 2023-07-31 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20230731_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='work',
        ),
    ]
