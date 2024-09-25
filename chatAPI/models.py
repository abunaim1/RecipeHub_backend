from django.db import models
from user.models import CustomUser

class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="uploads/profile", default="default.jpg")
    verified = models.BooleanField(default=False)
