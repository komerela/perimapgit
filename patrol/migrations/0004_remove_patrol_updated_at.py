# Generated by Django 2.2.6 on 2019-10-22 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patrol', '0003_patrol_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patrol',
            name='updated_at',
        ),
    ]
