# Generated by Django 5.2 on 2025-06-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appupdate',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('not_available', 'Not Available')], default='available', max_length=20),
        ),
    ]
