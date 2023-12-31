# Generated by Django 4.0.8 on 2023-10-30 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shed', '0003_remove_formdata_date_of_birth'),
        ('cow', '0008_cowregistration_actual_heat_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cowregistration',
            name='desease',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='CowDesease', to='cow.masterdesease'),
        ),
        migrations.AlterField(
            model_name='cowregistration',
            name='helth_status',
            field=models.CharField(choices=[('Good', 'Good'), ('Sick', 'Sick'), ('Natural', 'Natural')], default='Natural', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cowregistration',
            name='medicine',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='CowMedicine', to='cow.mastermedicin'),
        ),
        migrations.AlterField(
            model_name='cowregistration',
            name='shed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='CowRegistration', to='shed.shed_registration'),
        ),
        migrations.AlterField(
            model_name='cowregistration',
            name='vaccine',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='CowVaccine', to='cow.mastervaccine'),
        ),
    ]
