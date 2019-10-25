# Generated by Django 2.2.6 on 2019-10-21 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perimeters', '0001_initial'),
        ('floors', '0002_auto_20191020_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='floor',
            name='user',
        ),
        migrations.AddField(
            model_name='floor',
            name='perimeter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perimeters.Perimeter'),
        ),
    ]
