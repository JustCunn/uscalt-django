from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    number = models.CharField(max_length=50, default=None) 

    def __str__(self):
        return self.user.username