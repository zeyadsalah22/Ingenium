from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import high,questions,images


def index(request):
    return render(request,'ingenium/index.html')

def drama(request):
    return render(request,"ingenium/drama.html")

def music(request):
    return render(request,"ingenium/music.html")

def art(request):
    return render(request,"ingenium/art.html")

def photography(request):
    return render(request,"ingenium/photography.html")

def design(request):
    return render(request,"ingenium/design.html")

def media(request):
    return render(request,"ingenium/media.html")

def logistics(request):
    return render(request,"ingenium/logistics.html")

def hr(request):
    return render(request,"ingenium/hr.html")

def pr(request):
    return render(request,"ingenium/pr.html")

def literature(request):
    return render(request,"ingenium/literature.html")

