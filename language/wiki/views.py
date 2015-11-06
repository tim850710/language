from django.shortcuts import render
from wiki.models import Category,Page

def wiki(request):
    categories=Category.objects.order_by('-likes')
    context = {'categories':categories}
    return render(request, 'wiki/wiki.html', context)


def about(request):
    context = {}
    return render(request, 'wiki/about.html', context)