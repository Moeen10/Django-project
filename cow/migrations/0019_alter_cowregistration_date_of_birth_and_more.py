# Generated by Django 4.0.8 on 2023-11-01 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cow', '0018_alter_cowregistration_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cowregistration',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='cowregistration',
            name='next_vaccine_dose',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='cowregistration',
            name='purchase_date',
            field=models.DateField(null=True),
        ),
    ]
