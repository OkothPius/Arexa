# Generated by Django 3.2.5 on 2021-07-22 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0007_auto_20210722_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='head',
        ),
    ]