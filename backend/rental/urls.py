from django.urls import path
from .views import HomeListView

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home-list'),
]
