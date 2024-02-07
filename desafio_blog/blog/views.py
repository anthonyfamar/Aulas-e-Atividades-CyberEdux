from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .models import Post

def index(request):
    return HttpResponseRedirect ('/publicate')


def feed(request):
    return render(request, 'feed.html', {'posts': Post.objects.raw("SELECT * from blog_post")})


def publicate(request):
    if request.method == 'GET':
        return render(request, 'publicate')
    elif request.method == 'POST':
        author = request.POST.get('author')
        image = request.POST.get('image')
        content = request.POST.get('content')
        post = Post()
        post.author = author
        post.image = image
        post.content = content
        post.save()
        return HttpResponseRedirect('/feed')
    else:
        return HttpResponseBadRequest()
