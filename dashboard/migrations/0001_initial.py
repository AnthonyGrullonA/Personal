# Generated by Django 5.0.3 on 2024-03-06 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('posicion', models.CharField(max_length=100)),
                ('rango', models.CharField(max_length=100)),
            ],
        ),
    ]