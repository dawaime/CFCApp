# Generated by Django 5.0.1 on 2024-02-04 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_rename_individual_supporter_supporter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='supporter',
            name='status',
            field=models.CharField(max_length=55, null=True),
        ),
    ]
