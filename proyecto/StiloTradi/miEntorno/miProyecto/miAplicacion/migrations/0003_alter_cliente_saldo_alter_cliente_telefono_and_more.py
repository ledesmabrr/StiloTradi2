# Generated by Django 4.2.1 on 2023-05-24 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miAplicacion', '0002_alter_cliente_direccion_alter_proveedor_localidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Saldo',
            field=models.FloatField(help_text='the publisher precioCompra.'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Telefono',
            field=models.IntegerField(help_text='the publisher talle.'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='Fecha',
            field=models.DateField(help_text='the publisher description.'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='Total',
            field=models.FloatField(help_text='the publisher talle.'),
        ),
    ]
