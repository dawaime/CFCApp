# Generated by Django 5.0.1 on 2024-01-22 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_beneficiary_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary_request',
            name='comment',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
