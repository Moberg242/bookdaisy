# Generated by Django 4.2.15 on 2024-09-05 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='image_date',
            new_name='image_data',
        ),
    ]
