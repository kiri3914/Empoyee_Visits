# Generated by Django 4.0.2 on 2022-02-11 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=500)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('visited', models.BooleanField(default=False)),
                ('time_start', models.TimeField(blank=True, null=True)),
                ('time_end', models.TimeField(blank=True, null=True)),
                ('reason', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grid.employee')),
            ],
            options={
                'db_table': 'visit',
                'ordering': ['-date'],
            },
        ),
    ]
