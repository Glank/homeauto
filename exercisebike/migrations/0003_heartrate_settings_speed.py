# Generated by Django 4.2.11 on 2024-04-04 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercisebike', '0002_command_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeartRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True, db_index=True)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('value', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Speed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True, db_index=True)),
                ('value', models.FloatField()),
            ],
        ),
    ]