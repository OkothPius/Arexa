from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView
from .models import Rental


class HomeListView(ListView):

    models = Rental

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
