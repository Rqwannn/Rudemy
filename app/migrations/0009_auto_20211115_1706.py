# Generated by Django 3.2.8 on 2021-11-15 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_tags_profile_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
