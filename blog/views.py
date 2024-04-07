from django.shortcuts import render
from .models import Article

def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'articles': articles})

def readblog(request, article_id):
    articles = Article.objects.get(pk=article_id)
    return render(request, 'blog/readblog.html', {'articles': articles})
