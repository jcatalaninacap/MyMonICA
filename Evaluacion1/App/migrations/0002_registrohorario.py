# Generated by Django 5.1 on 2024-11-07 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroHorario',
            fields=[
                ('id_reg_horario', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_yymmdd', models.CharField(max_length=6)),
                ('hora_hhmm', models.CharField(max_length=4)),
                ('registros_validados', models.DecimalField(decimal_places=2, max_digits=10)),
                ('registros_preliminares', models.DecimalField(decimal_places=2, max_digits=10)),
                ('registros_no_validados', models.DecimalField(decimal_places=2, max_digits=10)),
                ('particula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.particula')),
            ],
        ),
    ]
