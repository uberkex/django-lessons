# Generated by Django 3.1.5 on 2021-01-17 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelrelation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('movies', models.ManyToManyField(to='modelrelation.Movie')),
            ],
        ),
    ]
