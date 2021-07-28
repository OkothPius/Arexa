from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from .models import Rental, Images

def home(request):
    return render(request, 'rental/base.html')

# def main(request):
#     return render(request, 'rental/main.html')

class MainView(generic.TemplateView):
    template_name = 'rental/main.html'


class HomeListView(generic.ListView):

    models = Rental
    queryset = Rental.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PostDetailView(generic.DetailView):
    models = Rental, Images

    def get_queryset(self):
        return Rental.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['images'] = Images.objects.all()
        return context


class SearchView(generic.TemplateView):
    template_name = 'rental/search.html'
    models = Rental

    def get_queryset(self):
        return Rental.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['search'] = Rental.objects.filter()
        return context
