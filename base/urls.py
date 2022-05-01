from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('detector/', views.detector, name="detector"),
    path('anpr/', views.anpr, name='anpr'),
    path('books/', views.books, name='books'),
]
