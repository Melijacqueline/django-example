# Generated by Django 4.1.7 on 2023-06-16 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_comercio', '0002_cliente_compracomputador_cliente_compramonitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='computador',
            name='imagen_producto',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='monitor',
            name='imagen_producto',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='mouse',
            name='imagen_producto',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
