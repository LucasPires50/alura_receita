# Generated by Django 3.2 on 2021-04-27 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0004_auto_20210427_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='date_receita',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 27, 11, 20, 7, 149113)),
        ),
    ]
