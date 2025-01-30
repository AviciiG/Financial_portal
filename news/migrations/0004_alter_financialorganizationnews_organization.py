# Generated by Django 4.2.18 on 2025-01-28 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_financialorganizationnews'),
        ('news', '0003_alter_financialorganizationnews_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialorganizationnews',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='organizations.financialorganization', verbose_name='Организация'),
        ),
    ]
