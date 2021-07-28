from django.urls import path
from .views import HomeListView, PostDetailView, SearchView
from . import views

app_name = 'rental'

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', HomeListView.as_view(), name='home-list'),
    path('rental/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('search/', SearchView.as_view(), name='search'),
]
