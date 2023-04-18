from django.shortcuts import render
from .models import Audio, Experimento
# Create your views here.

def experimento1(request):
    query = Experimento.objects.get(nome='Experimento 1')
    context = {
        'experimento' : query,
    }

    return render(request, 'experimento1.html', context)