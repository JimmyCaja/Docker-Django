# Generated by Django 4.0.5 on 2022-08-03 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ServicioTecnico', '0012_pedido_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='empleado',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ServicioTecnico.empleado'),
            preserve_default=False,
        ),
    ]
