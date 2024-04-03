from django.db import models
from datetime import timedelta
from django.utils import timezone

class Command(models.Model):
  text = models.CharField(max_length=128)
  time = models.DateTimeField(auto_now=True)
  def delete_too_old():
    old = Command.objects.filter(time__lte=timezone.now()-timedelta(minutes=1))
    print("Deleting {} too old cmds...".format(len(old)))
    old.delete()
