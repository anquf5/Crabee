# Generated by Django 3.2.8 on 2021-11-14 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20211111_1557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyreview',
            options={'ordering': ('-pub_date',)},
        ),
    ]