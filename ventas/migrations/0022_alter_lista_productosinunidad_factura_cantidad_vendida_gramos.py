# Generated by Django 5.0.3 on 2024-04-13 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0021_lista_productosinunidad_factura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista_productosinunidad_factura',
            name='cantidad_vendida_gramos',
            field=models.DecimalField(decimal_places=10, max_digits=15),
        ),
    ]