# Generated by Django 3.1 on 2021-11-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20211120_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='avatar/default.jpg', upload_to='avatar'),
            preserve_default=False,
        ),
    ]
