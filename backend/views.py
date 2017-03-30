from django.shortcuts import render


def login(request):
    context = {'names': ['Fellipe', 'Andre']}
    return render(request, 'login.html', context)
