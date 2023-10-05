# Generated by Django 4.2.5 on 2023-10-04 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='beneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_no', models.CharField(max_length=500, null=True)),
                ('name', models.CharField(max_length=55)),
                ('nationality', models.CharField(max_length=55)),
                ('date_of_birth', models.DateTimeField()),
                ('phone_number', models.CharField(max_length=20)),
                ('national_id', models.IntegerField()),
                ('national_address', models.CharField(max_length=255)),
                ('relationship', models.CharField(max_length=55)),
                ('is_qualified', models.IntegerField()),
                ('category', models.CharField(max_length=55)),
                ('marital_status', models.CharField(max_length=55)),
                ('is_benefiting', models.BooleanField(default=False)),
                ('inquiries', models.CharField(max_length=500)),
                ('justifications', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('account', models.CharField(max_length=55, null=True)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=55)),
                ('category', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='individual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('account', models.CharField(max_length=55, null=True)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=55)),
                ('category', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='orphan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('status', models.CharField(default=1, max_length=55)),
                ('justifications', models.CharField(max_length=500)),
                ('needs', models.TextField(max_length=500)),
                ('beneficiary_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.beneficiary')),
            ],
        ),
        migrations.CreateModel(
            name='supporter_operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=55)),
                ('category', models.CharField(max_length=55)),
                ('entity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.entity')),
            ],
        ),
        migrations.CreateModel(
            name='orphan_supporter_operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default=1, max_length=55)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('orphan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.orphan')),
                ('supporter_operation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.supporter_operation')),
            ],
        ),
        migrations.CreateModel(
            name='individual_supporter_operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default=1, max_length=55)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=55)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('individual_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.individual')),
                ('supporter_operation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.supporter_operation')),
            ],
        ),
    ]
