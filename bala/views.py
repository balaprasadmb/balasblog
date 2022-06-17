# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bala.models import Articles
from forms import ContactForm
from models import ContactDetails

from django.shortcuts import render

# Create your views here.
def home(request):
    articles = Articles.objects.all()
    return render(request, 'main.html', {'articles':articles})

def about(request):
    return render(request, 'about.html', locals())

def contact(request):
    message = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            city = form.cleaned_data['city']
            message = form.cleaned_data['message']
            contact_details = ContactDetails(name=name, email_id=email, phone=phone, city=city, message=message)
            contact_details.save()
            message = 'Thanks, We will Contact You Soon!'
    else:
        form = ContactForm(request.POST)
    return render(request, 'contact.html', {'form':form, 'message':message})

def show_articles(request, article_id):
    article = Articles.objects.get(pk=article_id)
    return render(request, 'article.html', {'article':article})
