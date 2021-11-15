# Generated by Django 3.2.8 on 2021-11-10 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('pub_time', models.DateTimeField()),
                ('topic_cont', models.CharField(max_length=1000)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-pub_time',),
            },
        ),
        migrations.CreateModel(
            name='TopicReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_time', models.DateTimeField()),
                ('reply_cont', models.CharField(max_length=1000)),
                ('replier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discussion.topic')),
            ],
            options={
                'ordering': ('-pub_time',),
            },
        ),
    ]
