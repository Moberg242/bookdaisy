# Generated by Django 4.2.15 on 2024-09-18 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_alter_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(choices=[(0, 'not read'), (1, 'hated it'), (2, 'disliked it'), (3, 'indifferent'), (4, 'liked it'), (5, 'loved it')], null=True),
        ),
    ]
