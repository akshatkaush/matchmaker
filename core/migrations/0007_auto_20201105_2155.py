# Generated by Django 3.1.2 on 2020-11-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201029_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='experience',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='job_role',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='salary_req',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='skills',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]