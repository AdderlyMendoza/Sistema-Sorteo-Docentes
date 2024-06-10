# Generated by Django 4.0 on 2024-05-20 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
            },
        ),
        migrations.CreateModel(
            name='Docentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('ap_paterno', models.CharField(max_length=50)),
                ('ap_materno', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=50)),
                ('escuela', models.CharField(max_length=50)),
                ('condicion', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Docente',
                'verbose_name_plural': 'Docentes',
            },
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignaciones', to='sorteo.area')),
                ('docente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sorteo.docentes')),
            ],
            options={
                'verbose_name': 'Asignacion',
                'verbose_name_plural': 'Asignaciones',
            },
        ),
    ]
