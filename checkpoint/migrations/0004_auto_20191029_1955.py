# Generated by Django 2.2.6 on 2019-10-29 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkpoint', '0003_auto_20191026_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkpoint',
            name='perimeter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perimeter_checkpoints', to='perimeters.Perimeter'),
        ),
    ]
