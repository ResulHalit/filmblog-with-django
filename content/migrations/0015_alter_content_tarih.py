# Generated by Django 3.2.13 on 2022-11-10 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_auto_20221110_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='tarih',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Yazı Tarihi'),
        ),
    ]
