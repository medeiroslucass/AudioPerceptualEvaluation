from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Audio, Experimento, Category
import random
import itertools




def get_categories(request):
    categories = Category.objects.all().values('id', 'name_category')
    return JsonResponse({'categories': list(categories)})
def experimento1(request):
    experimento = Experimento.objects.get(id=1)
    audios = Audio.objects.filter(form=experimento).order_by('row')
    grouped_audios = [list(group) for key, group in itertools.groupby(audios, lambda a: a.row)]
    random.shuffle(grouped_audios)


    if request.method == 'POST':
        print(request.POST)
        return redirect('experimento2')
    context = {
        'grouped_audios': grouped_audios,
        'experimento': experimento,
    }
    return render(request, 'experimento1.html', context)


def experimento2(request):
    experimento = Experimento.objects.get(id=2)
    audios = Audio.objects.filter(form=experimento).order_by('row')
    grouped_audios = [list(group) for key, group in itertools.groupby(audios, lambda a: a.row)]
    random.shuffle(grouped_audios)

    if request.method == 'POST':
        print(request.POST)
        return redirect('experimento3')

    context  = {
        'grouped_audios': grouped_audios,
        'experimento': experimento,
    }
    # print(request.POST)
    return render(request,  'experimento2.html', context)
def experimento3(request):
    experimento = Experimento.objects.get(id=3)
    audios = Audio.objects.filter(form=experimento).order_by('id')

    if request.method == 'POST':
        print(request.POST)

    context  = {
        'audios': audios,
        'experimento': experimento,
    }
    print(request.POST)
    return render(request,  'experimento3.html', context)
