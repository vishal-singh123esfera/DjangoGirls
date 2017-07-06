from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .form	import PostForm

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {})

def	post_new(request):
	form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

