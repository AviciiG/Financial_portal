# Generated by Django 4.2.18 on 2025-01-27 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_remove_financialorganization_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialorganization',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos/'),
        ),
    ]
