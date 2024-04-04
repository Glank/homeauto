from django.db import models
from datetime import timedelta
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

class Command(models.Model):
  #should be small enough that indexes arent necessary
  text = models.CharField(max_length=128)
  time = models.DateTimeField(auto_now=True)
  def delete_too_old():
    old = Command.objects.filter(time__lte=timezone.now()-timedelta(minutes=1))
    logger.debug("Deleting {} too old cmds...".format(len(old)))
    old.delete()

class Settings(models.Model):
  name = models.CharField(max_length=64)
  value = models.CharField(max_length=128)

class HeartRate(models.Model):
  time = models.DateTimeField(auto_now=True, db_index=True)
  value = models.FloatField()

class Speed(models.Model):
  time = models.DateTimeField(auto_now=True, db_index=True)
  value = models.FloatField()
