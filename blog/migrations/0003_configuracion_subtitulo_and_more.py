# Generated by Django 4.1.2 on 2022-10-21 02:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_configuracion_construido_por'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='subtitulo',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configuracion',
            name='titulo_principal',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
