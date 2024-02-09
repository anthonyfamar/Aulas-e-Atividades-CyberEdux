from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .models import Post

def index(request):
    return HttpResponseRedirect ('/feed')
    

def artigo(request):
    return render(request, 'artigo.html', {'posts': Post.objects.raw("SELECT * from blog_post")})


def feed(request):
    return render(request, 'feed.html', {'posts': Post.objects.raw("SELECT * from blog_post")})


def publicate(request):
    if request.method == 'GET':
        return render(request, 'publicate.html')
    elif request.method == 'POST':
        date = request.POST.get('date')
        author = request.POST.get('author')
        print(request.FILES)
        image = request.FILES['image']
        content = request.POST.get('content')
        post = Post()
        post.date = date
        post.author = author
        post.image = image
        post.content = content
        post.save()
        return HttpResponseRedirect('/feed')
    else:
        return HttpResponseBadRequest()
