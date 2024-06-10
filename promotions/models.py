from django.db import models

# Create your models here.

class Promotions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/promotions/')

    def __str__(self) -> str:
        return self.title