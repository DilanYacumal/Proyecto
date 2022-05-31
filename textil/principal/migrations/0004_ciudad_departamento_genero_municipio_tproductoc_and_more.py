# Generated by Django 4.0.4 on 2022-05-25 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_delete_authgroup_delete_authgrouppermissions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('idciudad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ciudad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('iddepartamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idgenero', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'genero',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('idmunicipio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TProductoC',
            fields=[
                ('idt_producto_c', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_producto', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 't_producto_c',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='ValorTela',
        ),
    ]