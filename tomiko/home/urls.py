from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('catalog', views.catalog),
    path('cards',views.cards),
    path('contacts',views.contacts),
    path('work',views.work),
    path('error', views.error_message)
]