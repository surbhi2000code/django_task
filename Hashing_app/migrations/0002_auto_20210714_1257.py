# Generated by Django 3.2.4 on 2021-07-14 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hashing_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
    ]