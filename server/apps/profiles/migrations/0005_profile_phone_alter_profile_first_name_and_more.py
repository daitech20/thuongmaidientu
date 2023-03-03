# Generated by Django 4.1.7 on 2023-03-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_address_recipient_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, default='dai', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, default='dai', max_length=50),
            preserve_default=False,
        ),
    ]
