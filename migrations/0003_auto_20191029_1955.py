# Generated by Django 2.2.6 on 2019-10-29 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patrolpoint', '0002_auto_20191021_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patrolpoint',
            name='patrol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patrolpoints', to='patrol.Patrol'),
        ),
    ]
