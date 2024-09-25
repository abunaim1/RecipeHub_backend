from django.db import models
from podcast.models import Podcast, PremimumPodcast

class PodcastEpisodeNormal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    audio = models.FileField(upload_to='podcasts/')
    author_name = models.CharField(max_length=100)
    publish_date = models.DateTimeField(auto_now_add=True)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class PodcastEpisodePremium(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    audio = models.FileField(upload_to='podcasts/')
    author_name = models.CharField(max_length=100)
    publish_date = models.DateTimeField(auto_now_add=True)
    podcast = models.ForeignKey(PremimumPodcast, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
