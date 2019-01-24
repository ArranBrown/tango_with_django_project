from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "Cruncy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)
    # return HttpResponse("Rango says hey there partner!, <br/> <a href='/rango/about/'>about </a>")


def about(request):
    context_dict = {'boldmessage': "Arran Brown"}
    return render(request, 'rango/about.html', context=context_dict)
    # #return HttpResponse("Rango says here is the about page <br/> <a href='/rango/'>Index </a>")
