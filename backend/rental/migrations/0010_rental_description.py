# Generated by Django 3.2.5 on 2021-08-16 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0009_images_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='description',
            field=models.TextField(default='Full Furnished'),
        ),
    ]
