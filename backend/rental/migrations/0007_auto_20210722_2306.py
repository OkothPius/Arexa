# Generated by Django 3.2.5 on 2021-07-22 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0006_auto_20210722_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='image_no',
        ),
        migrations.AlterField(
            model_name='images',
            name='head',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
