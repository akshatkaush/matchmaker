# Generated by Django 3.1.2 on 2020-10-28 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_jobposting_job_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='name',
        ),
        migrations.AddField(
            model_name='candidate',
            name='fname',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='lname',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]