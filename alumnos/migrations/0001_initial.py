# Generated by Django 5.1.4 on 2025-02-25 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('matricula', models.CharField(max_length=9, unique=True)),
                ('correo', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
