# Generated by Django 3.1 on 2021-11-19 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_company_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyreview',
            options={'ordering': ('-pub_time',)},
        ),
        migrations.RenameField(
            model_name='companyreview',
            old_name='pub_date',
            new_name='pub_time',
        ),
        migrations.RenameField(
            model_name='companyreview',
            old_name='rating',
            new_name='rate',
        ),
    ]