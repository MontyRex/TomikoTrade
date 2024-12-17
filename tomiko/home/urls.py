from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('catalog', views.catalog),
    path('cards',views.cards),
    path('contacts',views.contacts),
    path('work',views.work),
    path('error', views.error_message)
]