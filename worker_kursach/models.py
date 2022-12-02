from django.db import models

# Create your models here.
class Conference(models.Model):
    Title = models.TextField()
    ConfDate = models.TextField()
    ConfTag = models.TextField()
