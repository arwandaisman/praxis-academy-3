# Generated by Django 3.1.2 on 2020-10-28 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokoonline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='online',
            name='nomor_id',
            field=models.CharField(max_length=5, null=True, unique=True),
        ),
    ]
