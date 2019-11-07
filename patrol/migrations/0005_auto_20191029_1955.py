# Generated by Django 2.2.6 on 2019-10-29 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patrol', '0004_remove_patrol_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='patrol',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_patrols', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patrol',
            name='perimeter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patrols', to='perimeters.Perimeter'),
        ),
    ]