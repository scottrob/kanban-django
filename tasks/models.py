from django.db import models

class Cards(models.Model):
    title = models.CharField(max_length=255)
    # attachment = models.ImportField
    comments = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
