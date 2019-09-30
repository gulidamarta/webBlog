from django.shortcuts import render


def about(request):
    # return HttpResponse("About meeeee")
    return render(request, 'about.html')


def home(request):
    # return HttpResponse("Homepage")
    return render(request, 'homepage.html')


def contact(request):
    return render(request, 'contact.html')


def disclaimer(request):
    return render(request, 'disclaimer.html')

