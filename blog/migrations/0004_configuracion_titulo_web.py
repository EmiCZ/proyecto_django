# Generated by Django 4.1.2 on 2022-10-21 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_configuracion_subtitulo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='titulo_web',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]