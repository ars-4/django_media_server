# Generated by Django 4.0.4 on 2022-05-09 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_monthtimer_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthtimer',
            name='current',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 9, 14, 23, 5, 623032), null=True),
        ),
    ]
