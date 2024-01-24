# Generated by Django 5.0.1 on 2024-01-24 14:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_beneficiary_request_request_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiary',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
