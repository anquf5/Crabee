# Generated by Django 3.1 on 2021-11-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20211122_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='avatar/default.jpg', upload_to='avatar'),
        ),
    ]