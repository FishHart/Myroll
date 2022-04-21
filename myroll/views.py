from django.shortcuts import render

def myroll(request):
    for_range10 = [i for i in range(10)]

    return render(request, 'myroll/index.html', {'range10': for_range10})
