from django.urls import path
from .views import HomeListView
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', HomeListView.as_view(), name='home-list'),
]
