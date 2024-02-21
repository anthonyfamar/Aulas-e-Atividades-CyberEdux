from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    return HttpResponseRedirect ('/login')

def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.likes = post.likes + 1
    post.save()
    return HttpResponseRedirect(f'/artigo/{post_id}')

def artigo(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'artigo.html', {'post': post})


def feed(request):
    return render(request, 'feed.html', {'posts': Post.objects.raw("SELECT * from blog_post")})


@login_required(login_url='/login')
def publicate(request): 
    if request.method == 'GET':
        return render(request, 'publicate.html')
    elif request.method == 'POST':
        date = request.POST.get('date')
        #author = request.POST.get('author')
        author = request.user.first_name
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
    
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'incorrect_login': False 
        })
    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(request, email=email, senha=senha)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/feed')
        else:
            return render(request, 'login.html', {
                'incorrect_login': True 
            })
    else:
        return HttpResponseBadRequest()
    

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nomeCompleto = request.POST.get('nomeCompleto')
        nomeUsuario = request.POST.get('nomeUsuario')
        #dataNascimento = request.POST.get('dataNascimento')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.create_user(nomeUsuario, email, senha)
        user.first_name = nomeCompleto
        user.save()
        login(request, user)
        return HttpResponseRedirect('/feed')
    else:
        return HttpResponseBadRequest()
    