# Generated by Django 5.2 on 2025-04-27 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientprofile',
            name='agree_term_and_condition',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='google_uid',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='region',
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='address',
            field=models.TextField(default='Dodoma'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='password',
            field=models.CharField(default='00000000', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='phone_number',
            field=models.CharField(default='0762569852', max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='postal_code',
            field=models.CharField(default='41115', max_length=10),
            preserve_default=False,
        ),
    ]
