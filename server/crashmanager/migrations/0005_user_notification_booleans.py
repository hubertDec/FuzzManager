# Generated by Django 2.2.20 on 2021-06-18 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crashmanager', '0004_bugzillatemplate_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bucket_hit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='inaccessible_bug',
            field=models.BooleanField(default=False),
        ),
    ]