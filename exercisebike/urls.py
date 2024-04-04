from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('xbike/', views.index, name='index'),
  path('xbike/cmd', views.cmd, name='cmd'),
  path('xbike/sendcmd', views.send_cmd, name='send_cmd'),
]
