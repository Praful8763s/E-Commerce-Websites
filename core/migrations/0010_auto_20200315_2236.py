# Generated by Django 2.2 on 2020-03-15 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200315_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.CharField(default='1st January', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='time',
            field=models.CharField(default='08:00', max_length=7),
            preserve_default=False,
        ),
    ]
