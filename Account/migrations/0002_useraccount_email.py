# Generated by Django 3.1.7 on 2021-03-20 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='Email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
