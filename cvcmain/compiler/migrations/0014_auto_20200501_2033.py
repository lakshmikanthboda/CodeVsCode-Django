# Generated by Django 3.0.5 on 2020-05-01 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compiler', '0013_register_answered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answer',
            field=models.TextField(max_length=501),
        ),
    ]
