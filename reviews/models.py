from django.db import models

# Create your models here.
class Review(models.Model):
    full_name = models.CharField(
        max_length=100,)
    email = models.EmailField()
    rating = models.IntegerField()
    message = models.TextField(
        max_length=500,)

    def __str__(self):
        return f"{self.full_name} ({self.rating}/5)"