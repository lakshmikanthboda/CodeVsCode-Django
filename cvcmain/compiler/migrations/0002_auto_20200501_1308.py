# Generated by Django 3.0.5 on 2020-05-01 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compiler', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='register',
            options={'managed': True, 'verbose_name': 'register', 'verbose_name_plural': 'registers'},
        ),
        migrations.AlterModelTable(
            name='register',
            table='',
        ),
    ]
