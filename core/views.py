from django.shortcuts import render
from .models import Audio, Experimento

def evaluation_view(request):
    experimento = Experimento.objects.get(id=1)
    audios = Audio.objects.filter(category=experimento).order_by('id')

    if request.method == 'POST':
        print(request.POST)
    context = {
        'audios': audios,
        'experimento': experimento,
    }
    return render(request, 'partials/base_form.html', context)


def experimento2(request):
    return render(request)
def my_view(request):
    return render(request, 'teste.html')
