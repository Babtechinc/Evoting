# Generated by Django 3.1.7 on 2021-03-22 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electionposition',
            name='Status',
            field=models.CharField(blank=True, choices=[('open', 'Open'), ('close', 'Close')], default=[('open', 'Open'), ('close', 'Close')], max_length=255, null=True),
        ),
    ]