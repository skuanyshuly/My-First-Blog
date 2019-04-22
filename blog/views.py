from django.shortcuts import render
from . models import Post
from django.utils import timezone
# Create your views here.


def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts})

def series(request):
	return render(request, 'blog/series.html')

def free_episodes(request):
	return render(request, 'blog/free_episodes.html')

def gethbo(request):
	return render(request, 'blog/gethbo.html')

def index(request):
	return render(request, 'blog/index.html')





