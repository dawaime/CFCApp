# Generated by Django 5.0.7 on 2024-09-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_passwordcheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='national_id',
            field=models.CharField(default=0, max_length=20),
        ),
    ]