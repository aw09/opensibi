# Generated by Django 3.1.2 on 2020-11-11 23:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('method', models.CharField(max_length=200, null=True, unique=True)),
                ('status', models.CharField(max_length=230)),
                ('created_at', models.DateTimeField(default=datetime.datetime.utcnow)),
            ],
            options={
                'db_table': 'logs',
            },
        ),
    ]
