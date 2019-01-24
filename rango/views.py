from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage': "Cruncy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage': "Arran Brown"}
    return render(request, 'rango/about.html', context=context_dict)
