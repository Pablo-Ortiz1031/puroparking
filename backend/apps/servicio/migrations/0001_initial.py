# Generated by Django 5.2.3 on 2025-07-24 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(verbose_name='Nombre')),
                ('usuario_id', models.TextField(verbose_name='Usuario')),
                ('placa_vehiculo', models.TextField(verbose_name='Placa de vehiculo')),
            ],
        ),
    ]
