# Generated by Django 2.0.6 on 2019-06-02 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='celo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicioCelo', models.DateField()),
                ('fechaFinCelo', models.DateField()),
                ('fechaAplic', models.DateField()),
                ('nombreVacuna', models.CharField(max_length=60)),
            ],
        ),
    ]
