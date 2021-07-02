from django.db import models

class RoomInfo(models.Model):
    name = models.CharField(max_length=50)
    dev_name = models.CharField(max_length=50)
    brief_desc = models.TextField()

    def __str__(self):
        return self.name