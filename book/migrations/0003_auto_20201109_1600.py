# Generated by Django 3.1.2 on 2020-11-09 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20201108_0853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
