# Generated by Django 2.2.6 on 2019-10-21 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perimeters', '0001_initial'),
        ('patrol', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patrol',
            name='user',
        ),
        migrations.AddField(
            model_name='patrol',
            name='perimeter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perimeters.Perimeter'),
        ),
        migrations.AlterField(
            model_name='patrol',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]