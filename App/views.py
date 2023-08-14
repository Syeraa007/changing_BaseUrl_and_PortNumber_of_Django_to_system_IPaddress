from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def wish(request):
    return HttpResponse('<center><h1><b> This is First String Response after changing Base URL of Django </b></h1></center>')

def temp(request):
    return render(request,'temp.html')