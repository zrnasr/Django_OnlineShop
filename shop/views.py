from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'simple_page.html')


