from django.shortcuts import render

def catalogue_home(request):
    return render(request, 'home/about.html')