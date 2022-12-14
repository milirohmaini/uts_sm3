# Generated by Django 4.1.1 on 2022-10-06 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakultas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MahasiswaFkip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.CharField(max_length=50)),
                ('nama', models.CharField(max_length=100)),
                ('ttl', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('fakultas', models.CharField(max_length=100)),
                ('prodi', models.CharField(max_length=100)),
                ('alamat', models.CharField(max_length=300)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.RenameModel(
            old_name='Mahasiswa',
            new_name='DosenFkip',
        ),
        migrations.RenameField(
            model_name='dosenfkip',
            old_name='nim',
            new_name='nip',
        ),
    ]
