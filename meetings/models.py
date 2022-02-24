from django.db import models

class Meetings(models.Model):
    title = models.CharField(max_length = 200)
    date = models.DateField()
