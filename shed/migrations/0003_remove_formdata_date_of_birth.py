# Generated by Django 4.0.8 on 2023-10-25 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shed', '0002_formdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formdata',
            name='date_of_birth',
        ),
    ]