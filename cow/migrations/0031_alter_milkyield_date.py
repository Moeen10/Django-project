# Generated by Django 4.0.8 on 2023-11-12 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cow', '0030_alter_milkyield_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milkyield',
            name='date',
            field=models.DateField(),
        ),
    ]