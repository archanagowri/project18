from django.shortcuts import render

# Create your views here.

def boosers(request):
    return render(request,'boosers.html')