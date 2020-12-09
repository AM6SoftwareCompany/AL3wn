# Generated by Django 3.1 on 2020-12-09 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_applicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='email',
            field=models.EmailField(default='a@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='address',
            field=models.CharField(max_length=512, verbose_name='Address'),
        ),
    ]
