from django.urls import path
from .views import HomeListView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', HomeListView.as_view(), name='home-list'),
]
