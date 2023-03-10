# Generated by Django 4.0.5 on 2022-08-02 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServicioTecnico', '0007_delete_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nroSerie', models.CharField(max_length=13, verbose_name='Nro Serie')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('unidades', models.IntegerField(verbose_name='Unidades')),
                ('precioCompra', models.FloatField(verbose_name='Precio Compra')),
                ('precioVenta', models.FloatField(verbose_name='Precio Venta')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
            ],
        ),
    ]
