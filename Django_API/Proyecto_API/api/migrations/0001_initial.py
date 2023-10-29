# Generated by Django 3.2.4 on 2023-10-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField(max_length=4)),
                ('telefono', models.IntegerField(max_length=8)),
                ('sexo', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=60)),
                ('ciudad', models.CharField(max_length=50)),
            ],
        ),
    ]
