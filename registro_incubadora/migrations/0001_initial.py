# Generated by Django 4.2.7 on 2024-03-18 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('tiempo_encubacion', models.CharField(max_length=30)),
                ('tasa_mortalidad', models.CharField(max_length=50)),
                ('tasa_supervivencia', models.CharField(max_length=50)),
                ('evaluar_raza', models.CharField(max_length=50)),
                ('inversion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'registro',
            },
        ),
    ]
