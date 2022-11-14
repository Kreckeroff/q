from django.db import models

# Create your models here.
class Conference:
    def __init__(self, id,  Title, ConfDate, ConfTag):
        self.id = id
        self.Title = Title
        self.ConfDate = ConfDate
        self.ConfTag = ConfTag

class AddConference:
    def __init__(self,  Title, ConfDate, ConfTag):
        self.Title = Title
        self.ConfDate = ConfDate
        self.ConfTag = ConfTag
