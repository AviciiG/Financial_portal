# Generated by Django 4.2.18 on 2025-01-28 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_financialorganizationnews_source_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialorganizationnews',
            name='source_url',
            field=models.URLField(max_length=1000, verbose_name='Ссылка на источник'),
        ),
        migrations.AlterField(
            model_name='financialorganizationnews',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Заголовок'),
        ),
    ]
