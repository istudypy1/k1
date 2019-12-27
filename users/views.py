from django.shortcuts import render


def hello1(request):
    return render(request, 'users/index1.html')

