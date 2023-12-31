# Generated by Django 4.0.8 on 2023-11-01 10:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cow', '0015_alter_cowregistration_delivery_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cowregistration',
            name='purchase_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='cowregistration',
            name='active',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True),
        ),
    ]
