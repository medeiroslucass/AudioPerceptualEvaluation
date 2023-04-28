from django.urls import path, include
from . import views

urlpatterns = [
    path('exp1/', views.experimento1, name='experimento1'),
    path('exp2/', views.experimento2, name='experimento2'),
    path('exp3/', views.experimento3, name='experimento3'),
    path('get_categories/', views.get_categories, name='get_categories'),

]