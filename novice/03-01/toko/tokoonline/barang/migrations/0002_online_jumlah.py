# Generated by Django 2.2.12 on 2020-11-02 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='online',
            name='jumlah',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
