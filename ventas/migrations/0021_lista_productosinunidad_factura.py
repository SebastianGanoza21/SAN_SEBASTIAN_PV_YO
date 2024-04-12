# Generated by Django 5.0.3 on 2024-04-09 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0020_rename_stock_en_gramos_productosinunidad_stock_en_kilos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lista_ProductoSinUnidad_Factura',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_vendida_gramos', models.PositiveIntegerField()),
                ('codigo_factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.factura')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.productosinunidad')),
            ],
        ),
    ]
