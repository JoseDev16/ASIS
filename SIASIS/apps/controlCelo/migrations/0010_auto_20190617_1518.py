# Generated by Django 2.0.6 on 2019-06-17 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controlCelo', '0009_auto_20190617_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlcelo',
            name='celo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='controlCelo.Celo'),
        ),
    ]