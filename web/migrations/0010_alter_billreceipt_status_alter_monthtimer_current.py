# Generated by Django 4.0.4 on 2022-05-09 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_alter_monthtimer_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billreceipt',
            name='status',
            field=models.CharField(choices=[('Paid', 'paid'), ('Pending', 'pending')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='monthtimer',
            name='current',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 9, 14, 37, 50, 796059), null=True),
        ),
    ]
