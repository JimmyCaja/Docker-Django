# Generated by Django 4.0.5 on 2022-08-03 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ServicioTecnico', '0015_diagnostico_equipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='recibo',
            name='diagnostico',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='ServicioTecnico.diagnostico'),
            preserve_default=False,
        ),
    ]