# Generated by Django 4.1.1 on 2022-10-06 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakultas', '0008_mahasiswafkip_nomor'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosenfkip',
            name='nomor',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='stafffkip',
            name='nomor',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
