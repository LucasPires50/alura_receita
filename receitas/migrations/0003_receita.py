# Generated by Django 3.2 on 2021-04-27 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('receitas', '0002_delete_receita'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_receita', models.CharField(max_length=200)),
                ('ingredientes', models.TextField()),
                ('mode_preparo', models.TextField()),
                ('tempo_preparo', models.IntegerField()),
                ('rendimento', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('date_receita', models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 27, 9, 43, 4, 522350))),
            ],
            options={
                'db_table': 'alura_receitas',
            },
        ),
    ]
