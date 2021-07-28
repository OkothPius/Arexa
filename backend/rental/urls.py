from django.urls import path
from .views import HomeListView, PostDetailView, SearchView, MainView
from . import views

app_name = 'rental'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('home/', HomeListView.as_view(), name='home-list'),
    path('rental/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('search/', SearchView.as_view(), name='search'),
]
