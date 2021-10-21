import io
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from django.db.models import Q
from .models import Rental, Images
from .render import Render

from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

def home(request):
    return render(request, 'rental/base.html')

class MainView(generic.TemplateView):
    template_name = 'rental/main.html'

class HomeListView(generic.ListView):

    models = Rental
    queryset = Rental.objects.all()
    paginate_by = 10

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

#Search view
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

#Generate a PDF File houses List
def report_module(request):
    # Create ByteStream Buffer
    buf = io.BytesIO()
    #create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Add some lines of text
    lines = [
        "This is line 1",
        "This is line 2",
        "This is line 3",
    ]

    # Loop
    for line in lines:
        textob.textLine(line)

    # Finish Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    # Return Something
    return FileResponse(buf, as_attachment=True, filename='report.pdf')


# Generating PDF file for each specific listing
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
