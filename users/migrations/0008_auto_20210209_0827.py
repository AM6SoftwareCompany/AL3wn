# Generated by Django 3.1.4 on 2021-02-09 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210104_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='position',
            field=models.CharField(choices=[('PR', 'PR'), ('Customer Service', 'Customer Service')], max_length=255, verbose_name='Position'),
        ),
    ]
