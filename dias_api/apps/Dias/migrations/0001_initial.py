# Generated by Django 3.1.4 on 2022-01-23 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id_dia', models.DateField(primary_key=True, serialize=False)),
                ('tipo_fluxo', models.CharField(choices=[('FR', 'Fraca'), ('MD', 'Moderada'), ('FT', 'Forte'), ('IT', 'Intensa')], default='FR', max_length=2)),
                ('tipo_dor', models.CharField(choices=[('FR', 'Fraca'), ('MD', 'Moderada'), ('FT', 'Forte'), ('IT', 'Intensa')], default='FR', max_length=2)),
                ('tipo_TPM', models.CharField(choices=[('FR', 'Fraca'), ('MD', 'Moderada'), ('FT', 'Forte'), ('IT', 'Intensa')], default='FR', max_length=2)),
            ],
        ),
    ]