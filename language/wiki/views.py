from django.shortcuts import render


def wiki(request):
    context = {}
    return render(request, 'wiki/wiki.html', context)



def about(request):
    context = {}
    return render(request, 'wiki/about.html', context)