# Generated by Django 3.1.7 on 2021-03-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0002_auto_20210322_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electionposition',
            name='Status',
            field=models.CharField(blank=True, choices=[('open', 'Open'), ('closed', 'Closed')], default='Closed', max_length=255, null=True),
        ),
    ]
