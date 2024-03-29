# Generated by Django 3.2 on 2021-05-11 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=12, unique='True')),
                ('account_type', models.CharField(max_length=12)),
                ('username', models.CharField(max_length=50)),
                ('balance', models.FloatField()),
            ],
        ),
    ]
