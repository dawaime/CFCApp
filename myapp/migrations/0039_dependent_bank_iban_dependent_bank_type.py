# Generated by Django 5.0.7 on 2024-12-11 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0038_remove_beneficiary_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dependent',
            name='bank_iban',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='dependent',
            name='bank_type',
            field=models.CharField(max_length=64, null=True),
        ),
    ]