# Generated by Django 5.0.3 on 2024-03-15 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ACL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Telefono', models.IntegerField(null=True)),
                ('Celular', models.IntegerField(null=True)),
                ('Identificacion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_entrada', models.DateField(blank=True, null=True)),
                ('fecha_salida', models.DateField(blank=True, null=True)),
                ('autorizado_nap', models.BooleanField(default=False)),
                ('categoria', models.CharField(max_length=100, null=True)),
                ('Empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientdata.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Autorizador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Identificacion', models.CharField(max_length=100)),
                ('Posicion', models.CharField(max_length=100)),
                ('Empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clientdata.cliente')),
            ],
        ),
    ]
