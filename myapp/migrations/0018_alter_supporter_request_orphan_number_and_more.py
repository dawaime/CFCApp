# Generated by Django 5.0.1 on 2024-02-04 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_rename_amount_donated_supporter_beneficiary_sponsorship_amount_donated_monthly_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supporter_request',
            name='orphan_number',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='supporter_request',
            name='widower_number',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
