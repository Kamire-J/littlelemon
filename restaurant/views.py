from django.shortcuts import HttpResponse

# App views
def say_hello(request):
    return HttpResponse("Hey Jack!")
