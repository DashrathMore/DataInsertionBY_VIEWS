# Generated by Django 4.2.4 on 2023-08-22 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='name',
            new_name='Bname',
        ),
        migrations.CreateModel(
            name='reader',
            fields=[
                ('Rname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Date', models.DateField(auto_now=True)),
                ('Bname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.books')),
            ],
        ),
    ]
