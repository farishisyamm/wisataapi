# Generated by Django 3.2 on 2021-04-21 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wisata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('harga', models.CharField(max_length=50)),
                ('deskripsi', models.TextField()),
                ('lokasi', models.TextField()),
                ('gambar', models.URLField()),
            ],
        ),
    ]
