# Generated by Django 2.0.6 on 2019-06-03 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controlCelo', '0003_auto_20190602_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlcelo',
            name='celo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='controlCelo.Celo'),
        ),
    ]