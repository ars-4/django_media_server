# Generated by Django 4.0.4 on 2022-05-09 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_monthtimer_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthtimer',
            name='current',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
