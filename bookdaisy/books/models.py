from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField()
    author = models.CharField()
    genre = models.CharField()
    rating = models.IntegerField(blank=True, default=0)
    read = models.BooleanField()
    recommend = models.BooleanField(null=True)
    notes = models.TextField(max_length=200, null=True)
    image = models.ImageField(default='daisies.webp', blank=True)
    image_data = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                name='book_rating_range',
                check=models.Q(rating__range=(0, 5)),
                violation_error_message='Please rate 0-5'
            )
        ]
