from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .quiz import prefecture_quiz, quiz, wikipy


class IndexView(TemplateView):
    template_name = 'demo/index.html'


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.


class pref_quiz(TemplateView):
    template_name = 'demo/pref_quiz.html'
