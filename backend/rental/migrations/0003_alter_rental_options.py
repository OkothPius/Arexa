# Generated by Django 3.2.5 on 2021-07-09 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_alter_rental_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rental',
            options={'ordering': ['-pub_date']},
        ),
    ]