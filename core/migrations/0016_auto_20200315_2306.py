# Generated by Django 2.2 on 2020-03-15 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200315_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
        migrations.RemoveField(
            model_name='item',
            name='time',
        ),
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.CharField(max_length=15),
        ),
    ]
