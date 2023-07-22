from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    
    return render(request, "index1.html")
    

def statusRegister (request):
    
    username = request.POST["username"]
    password = request.POST["password"]

    usuario = User(
        username=username,
        password=password)
    
    usuario.save()
    
    """
        
        
        
    """
    return render(request, "send.html")

def pwa (request):
    
    return render(request, "index.html")
            
