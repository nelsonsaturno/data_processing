# Generated by Django 2.0.6 on 2018-06-25 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_auto_20180625_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='securityprice',
            name='weight',
        ),
        migrations.AddField(
            model_name='security',
            name='weight',
            field=models.FloatField(default=10.0),
        ),
    ]
