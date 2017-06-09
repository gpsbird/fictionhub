from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from posts.models import Post

def home(request):
    return render(request, 'pages/home.html', {
    })

def about(request):
    return render(request, 'pages/about.html', {
    })


def newsletter(request):
    return render(request, 'pages/newsletter.html', {
    })
