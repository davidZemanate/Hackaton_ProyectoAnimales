# Generated by Django 5.1.1 on 2024-10-17 20:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Animal Nombre')),
                ('edad', models.CharField(max_length=45, null=True)),
                ('tipo', models.CharField(max_length=45, verbose_name='Animal Tipo')),
                ('municipio', models.CharField(max_length=45)),
                ('departamento', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=45)),
                ('tipo_vulnerabilidad', models.CharField(choices=[('Abandono', 'Abandono'), ('Enfermedad', 'Enfermedad'), ('Maltrato', 'Maltrato')], max_length=45)),
                ('ayuda_requerida', models.CharField(max_length=45)),
                ('estado', models.TextField(null=True)),
                ('fecha_registro', models.DateTimeField(null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Persona Nombre')),
                ('telefono_contacto', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=45, verbose_name='Rol Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Usuario Nombre')),
                ('contrasena', models.CharField(max_length=45)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animales.persona')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animales.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Ayuda_Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=45, null=True)),
                ('descripcion', models.CharField(max_length=45, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animales.animal')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animales.usuario')),
            ],
        ),
    ]
