from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Command

def index(request):
  return render(request, "index.html", {})

def cmd(request):
  top = list(Command.objects.all()[:1])
  if len(top) == 0:
    return HttpResponse("")
  text = top[0].text
  top[0].delete()
  return HttpResponse(text)

def set_resistance(request, resistance):
  assert(0<=resistance<=9)
  command = Command(text="r{}".format(resistance))
  command.save()
  return redirect("index")
