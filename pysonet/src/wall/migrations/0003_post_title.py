# Generated by Django 3.1.4 on 2021-01-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_auto_20210108_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Статья'),
        ),
    ]
