from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import logging
import json
import re

from .models import Command

logger = logging.getLogger(__name__)

def home(request):
  return redirect('index')

def index(request):
  return render(request, "xbike/index.html", {})

def send_cmd(request):
  post_data = json.loads(request.body)
  command = Command(text=post_data['command'])
  logger.info("Sending command: '{}'".format(command.text))
  command.save()
  return redirect("index")

# is api method
@csrf_exempt
def cmd(request):
  if request.method == 'GET':
    return poll_cmd(request)
  else:
    return recieve_cmd(request)

def poll_cmd(request):
  Command.delete_too_old()
  top = list(Command.objects.all()[:1])
  if len(top) == 0:
    return HttpResponse("")
  text = top[0].text
  top[0].delete()
  return HttpResponse(text)

hr_command = re.compile(r'hr (\d*\.?\d+)')
def recieve_cmd(request):
  command = request.body.decode('utf-8')
  logger.info("Recieved command: '{}'".format(command))
  m = hr_command.match(command)
  if m:
    print("HR Command: {}".format(m.groups()))
  #TODO: if bad command return 400 code
  return HttpResponse('')
