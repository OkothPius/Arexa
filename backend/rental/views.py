from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from django.db.models import Q
from .models import Rental, Images
from .render import Render

def home(request):
    return render(request, 'rental/base.html')

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
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get('keyword')
        results = Rental.objects.filter(
            Q(estate__icontains=kw) | Q(title__icontains=kw) | Q(price__icontains=kw))
        print('results')
        context['results'] = results
        return context


class PdfView(generic.TemplateView):

    def get(self, request):
        rental = Rental.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'rental': rental,
            'request': request
        }
        return Render.render('rental/pdf.html', params)
