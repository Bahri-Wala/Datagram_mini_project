from django.db import models
from django.db import models

# Create your models here.
class Chain(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
