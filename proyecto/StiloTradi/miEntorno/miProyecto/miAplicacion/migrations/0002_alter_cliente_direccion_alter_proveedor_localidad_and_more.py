# Generated by Django 4.2.1 on 2023-05-24 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miAplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Direccion',
            field=models.CharField(help_text='the publisher talle.', max_length=50),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='Localidad',
            field=models.CharField(help_text='the publisher talle.', max_length=50),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='Direccion',
            field=models.CharField(help_text='the publisher talle.', max_length=50),
        ),
    ]
