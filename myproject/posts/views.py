from django.shortcuts import render
from .models import post 

# Create your views here.
def posts_list(request):
    posts = post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts':posts})

def  post_page(request, slug):
    posts = post.objects.get(slug=slug)
    return render(request, 'posts/posts_page.html', {'post':posts})

def post_new(request):
    return render(request, 'posts/post_new.html')