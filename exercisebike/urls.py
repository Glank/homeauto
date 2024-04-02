from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('xbike/cmd', views.cmd, name='cmd'),
  path('xbike/setresistance/<int:resistance>', views.set_resistance, name='set_resistance'),
]
