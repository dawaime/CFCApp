# Generated by Django 5.0.7 on 2024-11-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_alter_customuser_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
