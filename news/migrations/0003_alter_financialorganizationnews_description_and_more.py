# Generated by Django 4.2.18 on 2025-01-28 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_financialorganizationnews'),
        ('news', '0002_alter_financialorganizationnews_source_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialorganizationnews',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='financialorganizationnews',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_articles', to='organizations.financialorganization', verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='financialorganizationnews',
            name='published_date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
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
