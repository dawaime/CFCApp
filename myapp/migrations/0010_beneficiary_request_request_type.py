# Generated by Django 5.0.1 on 2024-01-24 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_beneficiary_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary_request',
            name='request_type',
            field=models.CharField(max_length=55, null=True),
        ),
    ]
