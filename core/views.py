from django.shortcuts import render
from core.models import *

def home(request):
    games = Games.objects.all()
    posts = Post.objects.all()
    news = News.objects.all()
    context = {
        'games': games,
        'posts': posts,
        'news': news,
    }
    return render(request,'index.html',context)

def games(request):
    games = Games.objects.order_by('-id')
    context = {
        'games': games,

    }

    return render(request,'games.html',context)

def dates(request):
   
    return render(request,'dates.html')

def detailpages(request,id):
    game = Games.objects.get(id=id)
    games = Games.objects.all()
    context = {
        'game':game,
        'games':games
    }
    return render(request,'detailpages.html',context)    
# Create your views here.
