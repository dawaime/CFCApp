# Generated by Django 5.0.1 on 2024-01-29 08:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_supporter_beneficiary_sponsorship_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Individual_supporter',
            new_name='Supporter',
        ),
        migrations.CreateModel(
            name='Supporter_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=55)),
                ('request_type', models.CharField(max_length=55, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=512, null=True)),
                ('reviewed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_supporter_set', to=settings.AUTH_USER_MODEL)),
                ('supporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.supporter')),
            ],
        ),
    ]
