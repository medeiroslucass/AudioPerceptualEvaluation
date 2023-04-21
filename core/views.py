from django.shortcuts import render
from .models import Audio

def evaluation_view(request):
    audios = Audio.objects.all()

    if request.method == 'POST':
        print(request.POST)
    context = {
        'audios': audios,
    }
    return render(request, 'experimento1.html', context)
