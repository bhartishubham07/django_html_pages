from django.shortcuts import render

# Create your views here.

def sample(request):
    return render(request, 'sample.html')

def index(request):
    return render(request, 'index.html')
