from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.evaluation_view, name='experimento1'),
]