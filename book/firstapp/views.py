from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'home.html')
    # return HttpResponse("<h1>hii i am fed up</h1>")


def offer(request):
    return render(request, 'offers.html')