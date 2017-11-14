# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bala.models import Articles

from django.shortcuts import render

# Create your views here.
def home(request):
    articles = Articles.objects.all()
    return render(request, 'main.html', {'articles':articles})

def about(request):
    return render(request, 'about.html', locals())

def contact(request):
    return render(request, 'contact.html')

def show_articles(request, article_id):
    article = Articles.objects.get(pk=article_id)
    return render(request, 'article.html', {'article':article})
