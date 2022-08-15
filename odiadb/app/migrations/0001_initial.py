# Generated by Django 3.2.15 on 2022-08-11 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllInfo',
            fields=[
                ('business_code', models.AutoField(primary_key=True, serialize=False)),
                ('person_name', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_category', models.CharField(blank=True, max_length=255, null=True)),
                ('details', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('suppliers', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=255, null=True)),
                ('whatsapp_no', models.CharField(blank=True, max_length=255, null=True)),
                ('email_id', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('contacted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='images/')),
            ],
        ),
    ]
