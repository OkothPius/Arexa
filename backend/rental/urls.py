from django.urls import path
from .views import HomeListView, PostDetailView
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', HomeListView.as_view(), name='home-list'),
    path('rental/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
]
