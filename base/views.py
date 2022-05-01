from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def detector(request):
    return render(request, 'base/detector.html')

def anpr(request):
    return render(request, 'base/anpr.html')

def books(request):
    return render(request, 'base/books.html')