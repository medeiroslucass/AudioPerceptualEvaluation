from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Audio, Experimento, Category, Usuario, Evaluation
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
        request.session.clear()
        exp1 = {}
        for key, value in request.POST.items():
            print(f'KEY: {key} VALUE: {value}')
            if key != 'csrfmiddlewaretoken':
                exp1[key] = value


        request.session[experimento.name] = exp1
        request.session.modified = True
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
        exp2 = {}
        for key, value in request.POST.items():
            print(f'KEY: {key} VALUE: {value}')
            if key != 'csrfmiddlewaretoken':
                exp2[key] = value


        request.session[experimento.name] = exp2
        print(f'2: {dict(request.session)}')
        return redirect('experimento3')

    context = {
        'grouped_audios': grouped_audios,
        'experimento': experimento,
    }
    # print(request.POST)
    return render(request,  'experimento2.html', context)
def experimento3(request):
    experimento = Experimento.objects.get(id=3)
    audios = Audio.objects.filter(form=experimento).order_by('id')

    grouped_audios = [list(group) for key, group in itertools.groupby(audios, lambda a: a.row)]
    random.shuffle(grouped_audios)
    if request.method == 'POST':
        exp3 = {}
        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                exp3[key] = value

        request.session[experimento.name] = exp3
        print(f'3 : {dict(request.session)}')
        return redirect('experimento4')

    context  = {
        'grouped_audios': grouped_audios,
        'experimento': experimento,
    }

    return render(request,  'experimento3.html', context)


def experimento4(request):
    experimento = Experimento.objects.get(id=4)
    audios = Audio.objects.filter(form=experimento).order_by('id')

    grouped_audios = [list(group) for key, group in itertools.groupby(audios, lambda a: a.row)]
    random.shuffle(grouped_audios)

    if request.method == 'POST':
        exp4 = {}
        for key, value in request.POST.items():
            if key  != 'csrfmiddlewaretoken':
                exp4[key] = value

        request.session[experimento.name] = exp4
        print(f'4 : {dict(request.session)}')
        return redirect('experimento5')

    context = {
        'grouped_audios': grouped_audios,
        'experimento': experimento,
    }

    return render(request, 'experimento4.html', context)


def experimento5(request):
    experimento = Experimento.objects.get(id=6)
    audios = Audio.objects.filter(form=experimento).order_by('id')

    grouped_audios = [list(group) for key, group in itertools.groupby(audios, lambda a: a.row)]
    random.shuffle(grouped_audios)

    if request.method == 'POST':
        print(f"POST : {request.POST}")
        exp5 = {}
        for key, value in request.POST.items():
            if key  != 'csrfmiddlewaretoken':
                exp5[key] = value

        request.session[experimento.name] = exp5
        print(f'5 : {dict(request.session)}')
        return redirect('usuario')

    context = {
        'grouped_audios': grouped_audios,
        'experimento': experimento,
    }

    return render(request, 'experimento5.html', context)


def usuario(request):
    if request.method == 'POST':
        usr = {}
        print(request.POST)
        for key,value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                usr[key] = value

        request.session['usr'] = usr
        print(request.session)
        # CREATE USER IN DB
        nome = request.session['usr']['nome']
        idade = request.session['usr']['idade']
        sexo = request.session['usr']['sexo']
        usuario = Usuario.objects.create(
            name=nome,
            age=idade,
            sex=sexo,
        )
        # REMOVE USR KEY
        request.session.pop('usr')
        # request.session.pop('Experimento 2')
        # request.session.pop('Experimento 3')
        # request.session.pop('Experimento 4')
        request.session.pop('Experimento 5')
        # SAVE DB
        for key, values in request.session.items():
            print('*' * 20)
            experimento = Experimento.objects.get(name=key)
            print(key)
            print(values)
            for id_audio, value in values.items():
                print(f'{id_audio}')
                print(f'Valor: {value}')
                numero_string = ''.join([char for char in id_audio if char.isdigit()])
                if numero_string:
                    numeric_part = int(numero_string)
                    print(numeric_part)
                    audio = Audio.objects.get(id=numeric_part)
                    evaluation = Evaluation.objects.create(
                        score=value,
                        audio_id=audio.id,
                        usuario_id=usuario.id,
                        form_id=experimento.id,
                    )
                else:
                    print("No numeric part found in the string")
        # print(dict(request.session))

    return render(request, 'usuario.html')
