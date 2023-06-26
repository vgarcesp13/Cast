from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#ruta de aplicacion home 

def home (request):
    return render(request,'navbar.html')