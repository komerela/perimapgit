# Generated by Django 2.2.6 on 2019-10-30 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floors', '0004_auto_20191029_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor',
            name='name',
            field=models.CharField(blank=True, help_text='Provide a name that can uniquely identify this floor on the perimeter', max_length=255, null=True),
        ),
    ]
