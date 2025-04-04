# Generated by Django 4.2 on 2025-04-04 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0002_alter_consulta_status_alter_medico_especialidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='status',
            field=models.CharField(choices=[('REA', 'REALIZADO'), ('AGEND', 'AGENDADO'), ('CANCEL', 'CANCELADO')], max_length=100),
        ),
        migrations.AlterField(
            model_name='medico',
            name='especialidade',
            field=models.CharField(choices=[('CLI', 'CLINICO'), ('ONCO', 'ONCOLOGISTA'), ('CARDIO', 'CARDIOLOGISTA')], max_length=40),
        ),
    ]
