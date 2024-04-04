from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Command

def home(request):
  return redirect('index')

def index(request):
  return render(request, "xbike/index.html", {})

def send_cmd(request):
  print(request.body)
  post_data = json.loads(request.body)
  print(post_data)
  command = Command(text=post_data['command'])
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

def recieve_cmd(request):
  command = request.body.decode('utf-8')
  print("Recieved Command: "+command)
  #TODO: if bad command return 400 code
  return HttpResponse('')
