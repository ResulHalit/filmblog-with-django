# Generated by Django 3.2.13 on 2022-11-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_auto_20221110_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='isim',
            field=models.CharField(max_length=100, null=True, verbose_name='Yazı Sahibi'),
        ),
        migrations.AlterField(
            model_name='content',
            name='tarih',
            field=models.DateField(null=True, verbose_name='Yazı Tarihi'),
        ),
    ]