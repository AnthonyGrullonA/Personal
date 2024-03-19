# Generated by Django 5.0.3 on 2024-03-15 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('nombre_empresa', models.CharField(max_length=200)),
                ('foto', models.ImageField(upload_to='imagenes/')),
                ('fecha_inicio_contrato', models.DateField()),
                ('direccion', models.CharField(max_length=200)),
                ('rnc', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Industria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_industria', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Industria',
                'verbose_name_plural': 'Industrias',
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localidad', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Localidad',
                'verbose_name_plural': 'Localidades',
            },
        ),
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operacion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Operacion',
                'verbose_name_plural': 'Operaciones',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sector', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Sector',
                'verbose_name_plural': 'Secotres',
            },
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id_contacto', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('nombre_contacto', models.CharField(max_length=100)),
                ('apellido_contacto', models.CharField(max_length=100)),
                ('identificacion', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=100)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientdata.cliente')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='industria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientdata.industria'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientdata.localidad'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_operacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientdata.operacion'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientdata.sector'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='status_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientdata.status'),
        ),
    ]