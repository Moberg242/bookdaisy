# Generated by Django 4.2.15 on 2024-09-28 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_alter_book_unique_together_alter_book_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to='books.profile'),
        ),
    ]
