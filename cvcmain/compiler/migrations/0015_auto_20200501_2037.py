# Generated by Django 3.0.5 on 2020-05-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compiler', '0014_auto_20200501_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='questions',
            name='inputs',
            field=models.TextField(max_length=502),
        ),
    ]
