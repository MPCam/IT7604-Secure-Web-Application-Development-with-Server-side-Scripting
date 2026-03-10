from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    cook_time_minutes = models.IntegerField()
    created_at = models.DateTimeField("Created")

    def __str__(self):
        return self.title