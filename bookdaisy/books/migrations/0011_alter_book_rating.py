# Generated by Django 4.2.15 on 2024-09-18 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_book_rating_alter_book_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(choices=[('Not read', 0), ('Hated it', 1), ('Didnt like', 2), ('It was okay', 3), ('Liked it', 4), ('Loved it', 5)], null=True),
        ),
    ]
