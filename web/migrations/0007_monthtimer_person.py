# Generated by Django 4.0.4 on 2022-05-09 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_monthtimer'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthtimer',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.person'),
        ),
    ]
