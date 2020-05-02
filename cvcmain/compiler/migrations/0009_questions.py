# Generated by Django 3.0.5 on 2020-05-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compiler', '0008_register_answers'),
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('question', models.CharField(max_length=1000)),
                ('inputs', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'register',
                'verbose_name_plural': 'registers',
                'db_table': '',
                'managed': True,
            },
        ),
    ]