from django.db import models

class Podcast(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    audio = models.FileField(upload_to='podcasts/')
    author_name = models.CharField(max_length=100)
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
