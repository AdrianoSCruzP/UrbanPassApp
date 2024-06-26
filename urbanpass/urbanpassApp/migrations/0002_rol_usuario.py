# Generated by Django 5.0.4 on 2024-04-27 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urbanpassApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.IntegerField(db_column='ID_Rol', primary_key=True, serialize=False)),
                ('rol', models.CharField(db_column='Rol', max_length=15)),
            ],
            options={
                'db_table': 'Rol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.IntegerField(db_column='ID_Usuario', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=20)),
                ('apellido', models.CharField(db_column='Apellido', max_length=20)),
                ('email', models.CharField(db_column='Email', max_length=30)),
                ('telefono', models.CharField(db_column='Telefono', max_length=9)),
                ('contrasena', models.CharField(db_column='Contrasena', max_length=200)),
            ],
            options={
                'db_table': 'Usuario',
                'managed': False,
            },
        ),
    ]
