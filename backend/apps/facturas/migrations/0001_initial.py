# Generated by Django 5.2.3 on 2025-07-24 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='facturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehiculo_id', models.IntegerField(verbose_name='Vehiculo')),
                ('total_pagar', models.IntegerField(verbose_name='Total a pagar')),
            ],
        ),
    ]
