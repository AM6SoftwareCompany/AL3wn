# Generated by Django 3.1.4 on 2021-03-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20210312_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bassemurl',
            name='kind',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('up', 'up'), ('perfect', 'perfect'), ('read', 'read'), ('bank', 'bank'), ('innovate', 'innovate')], max_length=255, verbose_name='Kind'),
        ),
    ]
