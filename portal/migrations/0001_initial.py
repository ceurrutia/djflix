# Generated by Django 4.2.2 on 2023-10-11 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=500, verbose_name='Nombre y Apellido')),
                ('direccion', models.CharField(max_length=700, verbose_name='Direccion')),
                ('dni', models.TextField(max_length=350, verbose_name='DNI')),
                ('email', models.CharField(max_length=250, verbose_name='Email')),
                ('pais', models.CharField(max_length=200, verbose_name='Pais')),
                ('ciudad', models.CharField(max_length=200, verbose_name='Ciudad')),
            ],
        ),
    ]
