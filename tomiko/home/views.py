from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def catalog(request):
    return HttpResponse("<h4>Это наш каталог</h4>")

#Переделать карточку
def cards(request):
    return HttpResponse("<h4>Карточка авто. Надо делать по-другому, отдельно</h4>")

def contacts(request):
    return HttpResponse("<h4>Контакты</h4>")

def work(request):
    return HttpResponse("<h4>Тут про работу</h4>")


#Это для тестов
def error_message(request):
    return HttpResponse("<h4>Непредвиденная ошибка</h4>")