from django.db import models

# Create your models here.
class recipe(models.Model):
    DIFFICULTY_CHOICES = [
        (1, 'Easy'),
        (2, 'Medium'),
        (3, 'Hard'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    favorite = models.BooleanField(default=False)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Recipe {self.id}: {self.title}"
