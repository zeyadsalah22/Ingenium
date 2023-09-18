from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import High,Question,Image


def index(request):
    highboards = High.objects.all().order_by('order')
    return render(request,'ingenium/index.html',{
        'highs':highboards
    })

def drama(request):
    images = Image.objects.filter(category='drama').order_by('order')
    questions = Question.objects.filter(category='drama').order_by('order')
    return render(request,"ingenium/drama.html",{
        'images':images[1:],
        'questions':questions
    })

def music(request):
    images = Image.objects.filter(category='music').order_by('order')
    questions = Question.objects.filter(category='music').order_by('order')
    return render(request,"ingenium/music.html",{
        'images':images[1:],
        'questions':questions
    })

def art(request):
    images = Image.objects.filter(category='art').order_by('order')
    questions = Question.objects.filter(category='art').order_by('order')
    return render(request,"ingenium/art.html",{
        'images':images[1:],
        'questions':questions
    })

def photography(request):
    images = Image.objects.filter(category='photography').order_by('order')
    questions = Question.objects.filter(category='photography').order_by('order')
    return render(request,"ingenium/photography.html",{
        'images':images[1:],
        'questions':questions
    })

def design(request):
    images = Image.objects.filter(category='design').order_by('order')
    questions = Question.objects.filter(category='design').order_by('order')
    return render(request,"ingenium/design.html",{
        'images':images[1:],
        'questions':questions
    })

def media(request):
    images = Image.objects.filter(category='media').order_by('order')
    questions = Question.objects.filter(category='media').order_by('order')
    return render(request,"ingenium/media.html",{
        'images':images[1:],
        'questions':questions
    })

def logistics(request):
    images = Image.objects.filter(category='logistics').order_by('order')
    questions = Question.objects.filter(category='logistics').order_by('order')
    return render(request,"ingenium/logistics.html",{
        'images':images[1:],
        'questions':questions
    })

def hr(request):
    images = Image.objects.filter(category='hr').order_by('order')
    questions = Question.objects.filter(category='hr').order_by('order')
    return render(request,"ingenium/hr.html",{
        'images':images[1:],
        'questions':questions
    })
def pr(request):
    images = Image.objects.filter(category='pr').order_by('order')
    questions = Question.objects.filter(category='pr').order_by('order')
    return render(request,"ingenium/pr.html",{
        'images':images[1:],
        'questions':questions
    })

def literature(request):
    images = Image.objects.filter(category='literature').order_by('order')
    questions = Question.objects.filter(category='literature').order_by('order')
    return render(request,"ingenium/literature.html",{
        'images':images[1:],
        'questions':questions
    })
