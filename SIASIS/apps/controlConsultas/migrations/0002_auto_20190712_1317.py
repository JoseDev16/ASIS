# Generated by Django 2.0 on 2019-07-12 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlConsultas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='proximaCita',
            field=models.DateField(null=True),
        ),
    ]
