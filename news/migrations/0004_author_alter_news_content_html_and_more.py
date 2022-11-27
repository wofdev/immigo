# Generated by Django 4.1.3 on 2022-11-26 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_author_alter_news_content_html_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('url', models.CharField(blank=True, max_length=2000)),
                ('avatar', models.CharField(blank=True, max_length=2000)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='content_html',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='news',
            name='date_published',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='news',
            name='summary',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.author'),
        ),
    ]