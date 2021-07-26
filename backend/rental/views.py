from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Rental, Images

def home(request):
    return render(request, 'rental/base.html')

def main(request):
    return render(request, 'rental/main.html')


class HomeListView(ListView):

    models = Rental
    queryset = Rental.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PostDetailView(DetailView):
    models = Rental, Images

    def get_queryset(self):
        return Rental.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['rental'] = Rental.objects.get(pk=id)
        context['images'] = Images.objects.all()
        return context
