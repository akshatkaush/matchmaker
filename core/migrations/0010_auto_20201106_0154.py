# Generated by Django 3.1.2 on 2020-11-05 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20201106_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='date_deadline',
            field=models.DateField(),
        ),
    ]