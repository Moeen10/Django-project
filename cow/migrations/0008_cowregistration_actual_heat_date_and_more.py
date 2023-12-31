# Generated by Django 4.0.8 on 2023-10-22 06:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cow', '0007_alter_sick_cow_cow_desease_alter_sick_cow_cow_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cowregistration',
            name='actual_heat_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cowregistration',
            name='delivery_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cowregistration',
            name='delivery_status',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='cowregistration',
            name='heat_status',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='cowregistration',
            name='pregnant_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cowregistration',
            name='provable_heat_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cowregistration',
            name='semen_push_status',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default=None, max_length=10),
        ),
    ]
