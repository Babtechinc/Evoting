# Generated by Django 3.1.7 on 2021-03-23 10:07

import Election.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0005_auto_20210322_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='electioncandidate',
            name='Electionmanifestoes',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=Election.models.create_path),
        ),
    ]
