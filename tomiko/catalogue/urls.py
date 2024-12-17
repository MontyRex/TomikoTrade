from django.urls import path
from . import views


urlpatterns = [
    path('', views.catalogue_home, name='catalogue_home')
]