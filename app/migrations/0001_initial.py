# Generated by Django 4.2.4 on 2023-08-22 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Liabrary',
            fields=[
                ('section', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('auther', models.CharField(max_length=100)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.liabrary')),
            ],
        ),
    ]
