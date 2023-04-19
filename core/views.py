from django.shortcuts import render, redirect
from .models import Audio, Experimento
from .forms import AudioForm

# from formtools.wizard.views import SessionWizardView
# from django.urls import reverse_lazy

# from .forms import AudioForm


def experimento1(request):
    experimento = Experimento.objects.get(nome='Experimento 1')
    audios = Audio.objects.filter(criterio=experimento)

    # Form
    form = AudioForm
    if request.method == 'POST':
        form = AudioForm(request.POST)
        print('chega aqui')
        print(f'form : {form}')
        print(form.is_valid)
        if form.is_valid():
            print('form valido')
            form.save()
            return redirect('teste_view')
    context = {
        'experimento' : experimento,
        'audios' : audios,
        'form' : form,
    }

    return render(request, 'experimento1.html', context)


def teste_view(request):
    return render(request, 'teste.html')
