# Generated by Django 3.2.5 on 2021-07-22 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_auto_20210722_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image_no',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='images',
            name='head',
            field=models.CharField(max_length=100),
        ),
    ]