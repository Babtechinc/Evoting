# Generated by Django 3.1.7 on 2021-03-20 20:33

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
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Password', models.CharField(blank=True, max_length=255, null=True)),
                ('NIN', models.CharField(blank=True, max_length=255, null=True)),
                ('DateIssued', models.DateField(blank=True, null=True)),
                ('VoteId', models.CharField(blank=True, max_length=255, null=True)),
                ('Lastname', models.CharField(blank=True, max_length=255, null=True)),
                ('Middlename', models.CharField(blank=True, max_length=255, null=True)),
                ('Firstname', models.CharField(blank=True, max_length=255, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('LocalGovernment', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]