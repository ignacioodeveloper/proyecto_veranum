# Generated by Django 5.0.4 on 2024-04-12 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_reserva_servicios_extra'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='reserva',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.estadoreserva'),
        ),
    ]
