# Generated by Django 3.2.8 on 2021-11-10 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_remove_company_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ('id',)},
        ),
    ]