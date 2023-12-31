# Generated by Django 4.2.3 on 2023-08-17 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(max_length=25)),
                ('raza', models.CharField(max_length=25)),
                ('nombre', models.CharField(max_length=25)),
                ('numeroContacto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Duenio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=60)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='PreguntasFrecuentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.TextField()),
                ('respuesta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('especialidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('situacion', models.CharField(max_length=25)),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='dueño',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.duenio'),
        ),
    ]
