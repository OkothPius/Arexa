from django.shortcuts import render
from django.views.generic import ListView


class HomeListView(ListView):
    template_name = 'home.html'
