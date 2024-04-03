from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('xbike/cmd', views.cmd, name='cmd'),
  path('xbike/sendcmd/<slug:command>', views.send_cmd, name='send_cmd'),
]
