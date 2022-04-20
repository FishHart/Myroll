from django.shortcuts import render

def myroll(request):
    return render(request, 'myroll/index.html', {})
