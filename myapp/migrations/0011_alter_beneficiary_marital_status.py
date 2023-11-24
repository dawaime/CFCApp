# Generated by Django 4.2.6 on 2023-10-25 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_beneficiary_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='marital_status',
            field=models.CharField(choices=[('married', 'متزوج/ـة'), ('single', 'أعزب/ـة'), ('widower', 'أرمل/ـة'), ('divorced', 'مطلقة')], max_length=55),
        ),
    ]