from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.experimento1, name='experimento1'),
    # path('wizard/', views.MeuWizard.as_view(), name='wizard'),
]