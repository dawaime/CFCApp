# Generated by Django 5.0.1 on 2024-03-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_support_operation_support_operation_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='support_operation',
            name='notes',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
