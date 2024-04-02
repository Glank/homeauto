from django.db import models

class Command(models.Model):
  text = models.CharField(max_length=128)
