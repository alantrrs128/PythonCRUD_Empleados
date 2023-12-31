# Generated by Django 4.2.6 on 2023-10-24 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=100)),
                ('apellidos', models.CharField(default='', max_length=100)),
                ('puesto', models.CharField(choices=[('RH', 'Recursos Humanos'), ('RI', 'Riesgos'), ('SE', 'Seguridad'), ('SI', 'Sistemas de Información'), ('TE', 'Tecnología'), ('DG', 'Digital'), ('DE', 'Director Ejecutivo'), ('DG', 'Director General'), ('DJ', 'Director Jurídico'), ('DT', 'Director Técnico')], max_length=2)),
                ('foto', models.FileField(upload_to='')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'empleados',
            },
        ),
    ]
