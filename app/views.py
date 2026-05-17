 

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import sys
import django
from datetime import datetime
def home(request):
    return HttpResponse("<h1>CI/CD Pipeline Demo</h1><p>Status: Successfully deployed via Jenkins & Docker on AWS!</p>")

def home(request):
    context = {
        'python_version': sys.version.split()[0],
        'django_version': django.get_version(),
        'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return render(request, 'app/index.html', context)

def portfolio(request):
    return render(request, 'app/portfolio.html')

def sandbox(request):
    return render(request, 'app/sandbox.html')