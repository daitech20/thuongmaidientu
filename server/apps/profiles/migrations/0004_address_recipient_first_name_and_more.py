# Generated by Django 4.1.7 on 2023-03-01 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='recipient_first_name',
            field=models.CharField(default='phuc', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='recipient_last_name',
            field=models.CharField(default='dai', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
