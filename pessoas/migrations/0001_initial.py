# Generated by Django 3.2 on 2021-04-27 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'pessoas',
            },
        ),
    ]
