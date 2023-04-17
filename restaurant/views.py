from django.shortcuts import render

# App views
def index(request):
    return render(request, 'index.html', {})