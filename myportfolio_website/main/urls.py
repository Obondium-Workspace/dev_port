#main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
        path('portfolio/<int:pk>/', views.portfolio_details, name='portfolio-details'),
]