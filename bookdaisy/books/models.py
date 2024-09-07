from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField()
    author = models.CharField()
    genre = models.CharField()
    rating = models.IntegerField()
    read = models.BooleanField()
    recommend = models.BooleanField()
    notes = models.TextField(max_length=200, null=True)
    image = models.FileField()
    image_data = models.BinaryField(null=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                name='book_rating_range',
                check=models.Q(rating__range=(0, 5)),
            )
        ]