from django.urls import path
from .views import (
            HomeListView, PostDetailView, RentalListView,
            SearchView, MainView, PdfView, RentalCreateView
            )
from . import views

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('home/', HomeListView.as_view(), name='home-list'),
    path('rental/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('download/', PdfView.as_view(), name='download'),
    path('house_pdf/', views.report_module, name='report'),
    path('rental/new/',RentalCreateView.as_view(), name='rental_create_new'),
    path('rental/sale/',RentalListView.as_view(), name='rental_list'), 
]
