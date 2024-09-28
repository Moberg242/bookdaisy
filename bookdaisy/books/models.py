from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField
from django.urls import reverse
from django.db.models.signals import post_save


# Create your models here.
class Book(models.Model):
    RATINGS = (
        (0, 'not read'),
        (1, 'hated it'),
        (2, 'disliked it'),
        (3, 'indifferent'),
        (4, 'liked it'),
        (5, 'loved it'),
    )

    POSITIONS = (
        (1, 'one'),
        (2, 'two'),
        (3, 'three'),
        (4, 'four'),
    )

    title = models.CharField()
    author = models.CharField()
    genre = models.CharField()
    rating = models.IntegerField(choices=RATINGS, default=0)
    read = models.BooleanField(default=False)
    recommend = models.BooleanField(null=True)
    notes = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(default='daisies.webp', blank=True)
    image_data = models.BinaryField(null=True, blank=True)
    color = ColorField(default='#FFFFFF')
    text_color = ColorField(default='000000')
    bookshelf = models.BooleanField(default=False)
    position = models.IntegerField(choices=POSITIONS, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.author}"
    
    def get_absolute_url(self):
        return reverse('book_details', kwargs={'pk': self.id})

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    darkTheme = models.BooleanField(default=False)
    color = ColorField(default='000000')
    follows = models.ManyToManyField("self",
        related_name="followed_by",
        symmetrical=False,
        blank=True)
    # https://www.youtube.com/watch?v=KNvSWubOaQY&list=PLCC34OHNcOtoQCR6K4RgBWNi3-7yGgg7b&index=3

    def __str__(self):
        if self.darkTheme:
            return f"{self.user} has dark theme enabled."
        else:
            return f"{self.user} has light theme enabled."
        

# create profile when user is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)