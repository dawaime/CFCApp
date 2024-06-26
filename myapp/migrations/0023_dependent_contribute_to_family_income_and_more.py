# Generated by Django 5.0.1 on 2024-02-20 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_customuser_second_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='dependent',
            name='contribute_to_family_income',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='dependent',
            name='disability_check',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='dependent',
            name='disability_type',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='dependent',
            name='employer',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='dependent',
            name='work_status',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
