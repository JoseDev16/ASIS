# Generated by Django 2.0.6 on 2019-06-03 01:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registroMascota', '0003_auto_20190602_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='dueñomascota',
            name='cuenta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='dueñomascota',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registroMascota.DueñoMascota'),
        ),
    ]