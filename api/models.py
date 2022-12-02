from django.db import models

# Create your models here.
class Conference:
    def __init__(self, Title, ConfDate, ConfTag):
        self.Title = Title
        self.ConfDate = ConfDate
        self.ConfTag = ConfTag