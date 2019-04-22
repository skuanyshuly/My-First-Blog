from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
path('', views.index, name='index'),
path('series', views.series, name='series'),
path('free_episodes', views.free_episodes, name='free_episodes'),
path('gethbo', views.gethbo, name='gethbo'),


	# path('main', views.main, name='main'),


]