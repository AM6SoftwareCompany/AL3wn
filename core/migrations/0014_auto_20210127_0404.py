# Generated by Django 3.1.4 on 2021-01-27 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210127_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outerexam',
            name='link',
            field=models.URLField(max_length=512),
        ),
    ]
