# Generated by Django 2.2.12 on 2020-11-02 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0005_auto_20201102_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='online',
            name='jumlah',
            field=models.IntegerField(blank=True, default=1000),
        ),
    ]
