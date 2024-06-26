# Generated by Django 5.0.1 on 2024-03-02 12:47

import django.db.models.deletion
import myapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_dependent_contribute_to_family_income_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support_operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('support_type', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('beneficiary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.beneficiary')),
            ],
        ),
        migrations.CreateModel(
            name='Support_operation_attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=256, null=True)),
                ('file_object', models.FileField(blank=True, null=True, upload_to=myapp.models.supporter_request_file_directory)),
                ('support_operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.support_operation')),
            ],
        ),
    ]
